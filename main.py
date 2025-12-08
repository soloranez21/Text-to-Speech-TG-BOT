"""
TTS Telegram Bot - Entry Point

A Telegram bot that converts text to speech using Gemini 2.5 Flash TTS.
"""

import asyncio
import logging

from src.bot.bot import create_bot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    """Start the bot."""
    logger.info("Starting TTS Bot...")
    bot, dp = create_bot()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
