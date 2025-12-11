"""
Gemini TTS integration using LangChain.

Handles text-to-speech generation using Gemini 2.5 Flash TTS model.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from google.ai.generativelanguage_v1beta.types import GenerationConfig

from src.config import settings


def create_tts_model():
    """Create a TTS model using Gemini 2.5 Flash TTS."""
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-tts",
        google_api_key=settings.google_api_key,
        response_modalities=[GenerationConfig.Modality.AUDIO],
    )


async def generate_speech(text: str) -> bytes | None:
    """Generate speech from text using Gemini TTS."""
    model = create_tts_model()
    response = model.invoke(text)

    audio_data = response.additional_kwargs.get("audio")
    if audio_data:
        return audio_data

    return None