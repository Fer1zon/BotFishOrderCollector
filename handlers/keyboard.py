from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

in_menu = InlineKeyboardButton(text = "В меню 🔙", callback_data="in_menu")

RC1 = InlineKeyboardButton(text = "НОВЫЙ ЛЕССНЕР", callback_data="НОВЫЙ ЛЕССНЕР")
RC2 = InlineKeyboardButton(text = "FAMILIA", callback_data="FAMILIA")
RC3 = InlineKeyboardButton(text = "АРИОСТО", callback_data="АРИОСТО")
RC4 = InlineKeyboardButton(text = "ГРАНД ВЬЮ", callback_data="ГРАНД ВЬЮ")
choice_rc_kb = InlineKeyboardBuilder().add(RC1, RC2, RC3, RC4).adjust(1).as_markup()

