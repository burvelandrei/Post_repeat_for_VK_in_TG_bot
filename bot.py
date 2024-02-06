import logging
import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='{filename}:{lineno} #{levelname:8} '
        '[{asctime}] - {name} - {message}',
        style='{'
    )

    logging.info("Starting BOT")

    config: Config = load_config()

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())