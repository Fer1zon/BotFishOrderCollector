from pathlib import Path
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.keyboard import in_menu, choice_rc_kb

from pathlib import Path

from utils.database_working import get_basket_products


async def get_welcome_message() -> dict:
    with open(Path("utils", "content", "welcome", "welcomeText.txt"), "r", encoding="UTF-8") as text_content:
        send_text = text_content.read()

    about_us = InlineKeyboardButton(text = "О нас", callback_data="about us")
    prices = InlineKeyboardButton(text = "Цены", callback_data="prices")
    get_sample = InlineKeyboardButton(text="Получить пробник", callback_data="get_sample")
    make_order = InlineKeyboardButton(text="Заказать", callback_data="make_order")
    send_keyboard = InlineKeyboardBuilder().add(about_us, get_sample, make_order, prices).adjust(1).as_markup()

    send_video = "BAACAgIAAxkBAAICUmeJEagXOT17abESKUy1hqI96WViAAKRYwAC-7RISMfZRy8hBWwxNgQ"
    
    return  {
        "text" : send_text,
        "video" : send_video,
        "keyboard" : send_keyboard
    }


async def about_us():
    with open(Path("utils","content","about_us","text.txt"), "r", encoding="UTF-8") as text_content:
        send_text = text_content.read()

    keyboard = InlineKeyboardBuilder().add(in_menu).adjust(1).as_markup()

    return {
        "text" : send_text,
        "keyboard" : keyboard
    }

async def prices():
    with open(Path("utils", "content", "prices", "text.txt"), "r", encoding = "UTF-8") as text_content:
        send_text = text_content.read()

    keyboard = InlineKeyboardBuilder().add(in_menu).adjust(1).as_markup()

    return {
        "text" : send_text,
        "keyboard" : keyboard
    }

    
    

async def make_order():
    with open(Path("utils", "content", "order", "text.txt"), "r", encoding = "UTF-8") as text_content:
        send_text = text_content.read()


    return {
        "text" : send_text,
        "keyboard" : choice_rc_kb
    }



async def order_ready(user_id : int):
    products = await get_basket_products(user_id=user_id)

    
    products_text = ""

    for item in products:
        products_text += f"{item.title} | {item.count} ШТ\n"

    send_text = f"""Ваш заказ:

{products_text}
Укажите контактные данные
"""

    return send_text



async def make_order_message_for_admin(user_id : int, contact_data : str, username : str, rc : str, delivery_time : str):
    products = await get_basket_products(user_id=user_id)

    
    products_text = ""

    for item in products:
        products_text += f"{item.title} | {item.count} ШТ\n"
    
    send_text = f"""
Заказ от @{username}
ЖК: {rc}
Дата: {delivery_time}
Контактные данные:
{contact_data}

Заказ:
{products_text}
"""

    return send_text



   

async def get_sample():
    send_video = FSInputFile(Path("utils","content", "sample","sample.MP4"))
    
    return {
        "video" : send_video
    }


async def get_sample_message():
    return """
"""




