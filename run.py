import asyncio
from importantFiles.config import dp, bot

from handlers.start import router as startRouter
from handlers.userHandlers.main import router as main_user_handler_router





async def main():


    dp.include_router(startRouter)
    dp.include_router(main_user_handler_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())