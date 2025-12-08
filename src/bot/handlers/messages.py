"""
Message handlers for the Telegram bot.

Handles text messages and file uploads (.md files).
"""

import io

from aiogram import Router, F, Bot
from aiogram.types import Message, BufferedInputFile
from aiogram.enums import ChatAction

from src.gemini.tts import generate_speech
from src.services.audio import pcm_to_mp3
from src.services.text import validate_text, extract_from_markdown

router = Router()


async def process_tts(message: Message, text: str):
    """Process text and send back audio."""
    # Validate text
    is_valid, result = validate_text(text)
    if not is_valid:
        await message.answer(f"❌ {result}")
        return

    # Send processing indicator
    status_msg = await message.answer("🎙 Генерирую аудио...")

    try:
        # Generate speech
        audio_data = await generate_speech(result)

        if not audio_data:
            await status_msg.edit_text("❌ Не удалось сгенерировать аудио. Попробуйте позже.")
            return

        # Convert to MP3
        mp3_data = pcm_to_mp3(audio_data)

        # Send audio file
        audio_file = BufferedInputFile(mp3_data, filename="speech.mp3")
        await message.answer_audio(audio_file)
        await status_msg.delete()

    except Exception as e:
        error_msg = "❌ Ошибка генерации. Попробуйте позже."
        if "429" in str(e):
            error_msg = "⏳ Сервис занят. Подождите немного и попробуйте снова."
        await status_msg.edit_text(error_msg)


@router.message(F.text)
async def handle_text(message: Message):
    """Handle text messages."""
    await message.bot.send_chat_action(message.chat.id, ChatAction.RECORD_VOICE)
    await process_tts(message, message.text)


@router.message(F.document)
async def handle_document(message: Message, bot: Bot):
    """Handle document uploads (.md files)."""
    doc = message.document

    # Check file extension
    if not doc.file_name or not doc.file_name.endswith(".md"):
        await message.answer("❌ Пожалуйста, отправьте .md файл или текстовое сообщение.")
        return

    # Download file
    file = await bot.get_file(doc.file_id)
    file_data = await bot.download_file(file.file_path)

    # Extract text
    content = file_data.read()
    text = extract_from_markdown(content)

    await bot.send_chat_action(message.chat.id, ChatAction.RECORD_VOICE)
    await process_tts(message, text)
