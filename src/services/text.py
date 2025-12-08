"""
Text processing service.

Handles text validation, length checking, and extraction from files.
"""

from src.config import settings

MAX_LENGTH = settings.max_text_length


def validate_text(text: str) -> tuple[bool, str]:
    """Validate text input for TTS processing.

    Returns:
        Tuple of (is_valid, message_or_cleaned_text)
    """
    if not text or not text.strip():
        return False, "Please send some text to convert to speech."

    cleaned = text.strip()
    if len(cleaned) > MAX_LENGTH:
        return False, f"Text too long. Maximum {MAX_LENGTH:,} characters. Your text: {len(cleaned):,} characters."

    return True, cleaned


def extract_from_markdown(content: bytes) -> str:
    """Extract text from markdown file content."""
    return content.decode("utf-8")
