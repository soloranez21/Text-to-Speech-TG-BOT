"""
Command handlers for the Telegram bot.

Handles /start and /help commands.
"""

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

WELCOME_TEXT = """Добро пожаловать в Text-to-Speech бот!

Отправьте мне текст или .md файл, и я преобразую его в речь.

Поддерживаемые языки: English, Русский, Deutsch (определяется автоматически)
Максимальная длина текста: 20,000 символов

Введите /help для подробной информации."""

HELP_TEXT = """Как использовать бот:

1. Отправьте текстовое сообщение - я преобразую его в речь
2. Загрузите .md файл - я прочитаю его вслух

Ограничения:
- Максимум 20,000 символов за запрос
- Поддержка: English, Русский, Deutsch

Голос: Kore (женский, естественный)

Просто отправьте текст, и я сгенерирую аудио!"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle /start command."""
    await message.answer(WELCOME_TEXT)


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command."""
    await message.answer(HELP_TEXT)
