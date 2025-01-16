from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatJoinRequest

from aiogram.fsm.context import FSMContext

from importantFiles.FSM import UserStates, AdminStates

from filters.adminFilters import IsAdmin


from utils.data_working import add_user_to_database
from handlers.keyboard import main_menu_kb

from importantFiles.config import bot







router = Router()

@router.message(F.photo, IsAdmin())
async def photo_id(message : Message):
    await message.reply(f"ID фотографии: {message.photo[0].file_id}")

@router.message(F.video, IsAdmin())
async def video_id(message : Message):
    await message.reply(f"ID видео: {message.video.file_id}")


@router.message(CommandStart())
async def start_user(message : Message, state : FSMContext):
    add_user_to_database(message.from_user.id)

    send_video = "AgACAgIAAxkBAAMFZ4ecaQr-Qmqsje92WsZtGpUTi50AAoHmMRtCeUBIck1Flyji1Y4BAAMCAANzAAM2BA"
    send_text = """Добрый день, уважаемые соседи! 🌞 

Приём заявок на пробники завершён. Благодарим всех, кто принял участие! ❤️ Надеемся, вам понравилась наша рыба. 

Теперь вы можете оформить предзаказ на охлаждённый лосось. Бесплатная доставка осуществляется каждую неделю по четвергам и пятницам. Доступны следующие варианты: 
- Филе (кусок) 
- Предголовная часть 
- Хвостовая часть 
- Целая рыба 
Оставляйте заявку, и наш менеджер свяжется с вами для согласования всех деталей доставки и заказа. 🛒✨"""
    await message.answer_video(caption=send_text, video=send_video, reply_markup=main_menu_kb)
    #await message.answer(send_text, reply_markup=main_menu_kb)
    


    await state.set_state(UserStates.MAIN_MENU)



    