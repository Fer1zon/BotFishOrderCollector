from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatJoinRequest

from aiogram.fsm.context import FSMContext

from importantFiles.FSM import UserStates, AdminStates

from filters.adminFilters import IsAdmin


from utils.json_data_working import add_user_to_database


from importantFiles.config import bot

from utils.message_making import get_welcome_message

from utils.database_working import clear_basket






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
    await clear_basket(message.from_user.id)


    message_content = await get_welcome_message()
    send_video = message_content["video"]
    send_text = message_content["text"]
    main_menu_kb = message_content["keyboard"]
    
    try:
        await message.answer_video(caption=send_text, video=send_video, reply_markup=main_menu_kb)
    except:
        await message.answer(send_text, reply_markup=main_menu_kb)
    #await message.answer(send_text, reply_markup=main_menu_kb)
    


    await state.set_state(UserStates.MAIN_MENU)



    