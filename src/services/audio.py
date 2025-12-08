"""
Audio conversion service.

Handles PCM to MP3 conversion using pydub.
"""

import io
import wave

from pydub import AudioSegment


def pcm_to_wav(pcm_data: bytes, sample_rate: int = 24000, channels: int = 1, sample_width: int = 2) -> bytes:
    """Convert raw PCM data to WAV format."""
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_data)
    wav_buffer.seek(0)
    return wav_buffer.read()


def wav_to_mp3(wav_data: bytes) -> bytes:
    """Convert WAV audio to MP3 format."""
    audio = AudioSegment.from_wav(io.BytesIO(wav_data))
    mp3_buffer = io.BytesIO()
    audio.export(mp3_buffer, format="mp3")
    mp3_buffer.seek(0)
    return mp3_buffer.read()


def pcm_to_mp3(pcm_data: bytes) -> bytes:
    """Convert raw PCM data directly to MP3."""
    wav_data = pcm_to_wav(pcm_data)
    return wav_to_mp3(wav_data)
