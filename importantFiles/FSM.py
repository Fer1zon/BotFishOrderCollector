from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    MAIN_MENU = State()


class AdminStates(StatesGroup):
    MAIN_MENU = State()