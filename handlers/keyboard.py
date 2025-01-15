from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

in_menu = InlineKeyboardButton(text = "В меню 🔙", callback_data="in_menu")

get_sample = InlineKeyboardButton(text="Получить пробник ✅", callback_data="get_sample")
make_order = InlineKeyboardButton(text="Оставить предзаказ", callback_data="make_order")
main_menu_kb = InlineKeyboardBuilder().add(get_sample, make_order).adjust(1).as_markup()

RC1 = InlineKeyboardButton(text = "НОВЫЙ ЛЕССНЕР", callback_data="НОВЫЙ ЛЕССНЕР")
RC2 = InlineKeyboardButton(text = "FAMILIA", callback_data="FAMILIA")
RC3 = InlineKeyboardButton(text = "АРИОСТО", callback_data="АРИОСТО")
RC4 = InlineKeyboardButton(text = "ГРАНД ВЬЮ", callback_data="ГРАНД ВЬЮ")
choice_rc_kb = InlineKeyboardBuilder().add(RC1, RC2, RC3, RC4).adjust(1).as_markup()

