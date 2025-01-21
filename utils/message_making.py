from pathlib import Path
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_welcome_message() -> dict:
    with open(Path("utils", "content", "welcomeText.txt"), "r", encoding="UTF-8") as text_content:
        send_text = text_content.read()

    get_sample = InlineKeyboardButton(text="Получить пробник ✅", callback_data="get_sample")
    make_order = InlineKeyboardButton(text="Оставить предзаказ", callback_data="make_order")
    send_keyboard = InlineKeyboardBuilder().add(make_order).adjust(1).as_markup()

    send_video = "BAACAgIAAxkBAAICUmeJEagXOT17abESKUy1hqI96WViAAKRYwAC-7RISMfZRy8hBWwxNgQ"
    
    return  {
        "text" : send_text,
        "video" : send_video,
        "keyboard" : send_keyboard
    }
