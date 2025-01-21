import asyncio
from importantFiles.config import dp, bot

from handlers.start import router as startRouter
from handlers.userHandlers.main import router as main_user_handler_router

from utils.data_working import create_json_file
import logging
logger = logging.getLogger(__name__)





async def main():
    if create_json_file():
        logger.info("JSON database creates")

    else:
        logger.info("JSON database exists")

    dp.include_router(startRouter)
    dp.include_router(main_user_handler_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())