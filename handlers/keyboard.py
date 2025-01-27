from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

in_menu = InlineKeyboardButton(text = "В меню 🔙", callback_data="in menu")

RC1 = InlineKeyboardButton(text = "НОВЫЙ ЛЕССНЕР", callback_data="НОВЫЙ ЛЕССНЕР")
RC2 = InlineKeyboardButton(text = "FAMILIA", callback_data="FAMILIA")
RC3 = InlineKeyboardButton(text = "АРИОСТО", callback_data="АРИОСТО")
RC4 = InlineKeyboardButton(text = "ГРАНД ВЬЮ", callback_data="ГРАНД ВЬЮ")
choice_rc_kb = InlineKeyboardBuilder().add(RC1, RC2, RC3, RC4).adjust(1).as_markup()


salmon = InlineKeyboardButton(text = "Лосось", callback_data = "Лосось")
trout = InlineKeyboardButton(text = "Форель", callback_data="Форель")
choice_fish_type_kb = InlineKeyboardBuilder().add(salmon, trout).adjust(2).as_markup()


yes = InlineKeyboardButton(text = "Еще", callback_data="Ещё")
place_an_order = InlineKeyboardButton(text = "Оформить заказ", callback_data="Оформить")
making_order = InlineKeyboardBuilder().add(yes, place_an_order).adjust(2).as_markup()
