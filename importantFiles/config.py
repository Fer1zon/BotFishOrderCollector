import logging.handlers
import os
from dotenv import load_dotenv

import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from pathlib import Path



from datetime import datetime


load_dotenv()
TOKEN = os.environ['TOKEN']
admins = [int(admin_id) for admin_id in os.environ['ADMINS'].split(',')]
SEND_ORDER_CHAT_ID = os.environ["SEND_ORDER_CHAT_ID"]


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








