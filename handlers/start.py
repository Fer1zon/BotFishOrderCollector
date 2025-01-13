from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from importantFiles.FSM import UserStates, AdminStates

from filters.adminFilters import IsAdmin

from utils.database.user import add_user





router = Router()





@router.message(CommandStart(), IsAdmin())
async def start_admin(message : Message, state : FSMContext):
    send_text = "Привет, Администратор!"
    await message.answer(send_text)
    
    await state.set_state(AdminStates.MAIN_MENU)


@router.message(CommandStart())
async def start_user(message : Message, state : FSMContext):
    send_text = "Привет, Пользователь!"
    await message.answer(send_text)

    await state.set_state(UserStates.MAIN_MENU)



    