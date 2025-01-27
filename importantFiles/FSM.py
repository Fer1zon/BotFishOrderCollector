from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    MAIN_MENU = State()
    CHOICE_RESIDENTIAL_COMPLEX = State()
    CHOICE_TIME_DELIVERY = State()
    INPUT_CONTACT_DATA = State()

    CHOICE_RESIDENTIAL_COMPLEX_ORDER = State()
    CHOICE_TIME_DELIVERY_ORDER = State()
    CHOICE_FISH_TYPE_ORDER = State()
    CHOICE_PRODUCT_ORDER = State()
    INPUT_COUNT_PRODUCT_ORDER = State()
    INPUT_CONTACT_DATA_ORDER = State()




class AdminStates(StatesGroup):
    MAIN_MENU = State()