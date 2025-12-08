"""
Telegram Bot initialization and setup.

This module handles the bot instance creation and dispatcher configuration.
"""

from aiogram import Bot, Dispatcher

from src.config import settings
from src.bot.handlers import commands, messages


def create_bot() -> tuple[Bot, Dispatcher]:
    """Create and configure the bot and dispatcher."""
    bot = Bot(token=settings.telegram_bot_token)
    dp = Dispatcher()

    # Register handlers
    dp.include_router(commands.router)
    dp.include_router(messages.router)

    return bot, dp
