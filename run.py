import asyncio
from importantFiles.config import createTables, dp, bot

from scheduler.main import scheduler

from handlers.start import router as startRouter





async def main():
    await createTables()

    scheduler.start()

    dp.include_router(startRouter)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())