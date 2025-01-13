import logging.handlers
import os
from dotenv import load_dotenv

import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from importantFiles.database.models import Model


from datetime import datetime


load_dotenv()
TOKEN = os.environ['TOKEN']
admins = [int(admin_id) for admin_id in os.environ['ADMINS'].split(',')]



data_base_path = str(Path("importantFiles","database","data_base.db"))

dbEngine = create_async_engine(
    "sqlite+aiosqlite:///" + data_base_path
)
new_session = async_sessionmaker(dbEngine, expire_on_commit=False)

async def createTables():
    async with dbEngine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


logging.basicConfig(
                    level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=Path("importantFiles", "log.log"),
                    encoding="UTF-8"
                    )

logging.info("--------------------------START--------------------------")
logger = logging.getLogger(__name__)






bot = Bot(token=os.environ["TOKEN"], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())








