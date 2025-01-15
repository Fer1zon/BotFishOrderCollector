from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from importantFiles.FSM import UserStates, AdminStates

from filters.adminFilters import IsAdmin


from utils.data_working import add_user_to_database
from handlers.keyboard import main_menu_kb







router = Router()



@router.message(CommandStart())
async def start_user(message : Message, state : FSMContext):
    add_user_to_database(message.from_user.id)

    send_img = "AgACAgIAAxkBAAMFZ4ecaQr-Qmqsje92WsZtGpUTi50AAoHmMRtCeUBIck1Flyji1Y4BAAMCAANzAAM2BA"
    send_text = """Добрый день, соседи! 🌞

Мы — магазин "Рыба в сети" — запускаем доставку охлаждённой красной рыбы! 🚚🐟 В рамках тестирования сервиса вы можете получить бесплатный пробник филе лосося (250–300 г).

✔ Это премиальное мурманское филе, не подвергавшееся заморозке, свежее и высокого качества.

Чтобы попробовать, жмите "Получить пробник". Если уже получали пробник и хотите сделать предзаказ рыбы, нажимайте "Оставить предзаказ". 🛒✨"""
    await message.answer_photo(caption=send_text, photo=send_img, reply_markup=main_menu_kb)


    await state.set_state(UserStates.MAIN_MENU)



    