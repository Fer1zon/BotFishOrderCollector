from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from importantFiles.FSM import UserStates
from handlers.keyboard import choice_rc_kb

from aiogram.exceptions import TelegramBadRequest

from utils.keyboard_maker import get_datetime_order_kb


import logging

from datetime import datetime

from importantFiles.config import SEND_ORDER_CHAT_ID, bot

from utils.data_working import check_get_sample, edit_contact_data, change_get_sample, get_contact_data
from utils.message_making import get_welcome_message


router = Router()
logger = logging.getLogger(__name__)



@router.callback_query(F.data == "get_sample", UserStates.MAIN_MENU)
async def get_sample(call : CallbackQuery, state : FSMContext):
    if check_get_sample(call.from_user.id):
        return await call.answer("Вы уже получали пробник!")
    send_text = "Выберите ваш ЖК для доставки:"

    try:
        await call.message.edit_text(text = send_text, reply_markup=choice_rc_kb)
        await state.set_state(UserStates.CHOICE_RESIDENTIAL_COMPLEX)

    except TelegramBadRequest:
        await call.message.answer(text = send_text, reply_markup=choice_rc_kb)
        await state.set_state(UserStates.CHOICE_RESIDENTIAL_COMPLEX)
    
    except Exception as ex:
        logger.error(f"Error in get_sample handler: {str(ex)}")
        await call.answer(text = "Произошла ошибка, попробуйте позже.")

    
        

@router.callback_query(F.data.in_({"НОВЫЙ ЛЕССНЕР", "FAMILIA", "АРИОСТО", "ГРАНД ВЬЮ"}), UserStates.CHOICE_RESIDENTIAL_COMPLEX)
async def choice_residential_complex(call : CallbackQuery, state : FSMContext):
    await state.update_data(rc = call.data)

    send_text = "Выберите дату и время доставки:"
    keyboard = get_datetime_order_kb()

    try:
        await call.message.edit_text(text = send_text, reply_markup=keyboard)
        await state.set_state(UserStates.CHOICE_TIME_DELIVERY)

    except TelegramBadRequest:
        await call.message.answer(text = send_text, reply_markup=keyboard)
        await state.set_state(UserStates.CHOICE_TIME_DELIVERY)
    
    except Exception as ex:
        logger.error(f"Error in choice_residential_complex handler: {str(ex)}")
        await call.answer(text = "Произошла ошибка, попробуйте позже.")

    
        

@router.callback_query(F.data.not_in({"in_menu"}), UserStates.CHOICE_TIME_DELIVERY)
async def choice_time_delivery(call : CallbackQuery, state : FSMContext):

    
    
    
    
    contact_data = get_contact_data(call.from_user.id)
    if not contact_data:
        await state.update_data(sample_datetime = call.data)

        send_text = """Пожалуйста, напишите ваше имя и номер телефона для связи: 
Эта информация нужна, чтобы мы могли уточнить детали доставки.😊"""

        try:
            await call.message.edit_text(text = send_text)
            await state.set_state(UserStates.INPUT_CONTACT_DATA)

        except TelegramBadRequest:
            await call.message.answer(text = send_text)
            await state.set_state(UserStates.INPUT_CONTACT_DATA)
        
        except Exception as ex:
            logger.error(f"Error in choice_time_delivery handler: {str(ex)}")
            await call.answer(text = "Произошла ошибка, попробуйте позже.")

        
            

        return
    
    send_text = "Спасибо ваша заявка принята."

    await call.answer(send_text)
    
    message_content = await get_welcome_message()
    send_video = message_content["video"]
    send_text = message_content["text"]
    main_menu_kb = message_content["keyboard"]
    
    


    

    try:
        await call.message.delete()
    except:
        pass
    await call.message.answer_video(caption=send_text, video=send_video, reply_markup=main_menu_kb)
    #await message.answer(send_text, reply_markup=main_menu_kb)
    await state.set_state(UserStates.MAIN_MENU)

    
        
    data = await state.get_data()

    send_text = f"""
<b>Пробник</b>
<b>Пользователь:</b> @{call.from_user.username}
<b>ЖК:</b> <i>{data["rc"]}</i>
<b>Дата получения:</b> <code>{call.data}</code>

<b>Контактные данные:</b>
<i>{contact_data}</i>"""
    
    await bot.send_message(chat_id=SEND_ORDER_CHAT_ID, text = send_text)

    
    change_get_sample(user_id=call.from_user.id)
    


@router.message(F.text, UserStates.INPUT_CONTACT_DATA)
async def input_contact_data(message : Message, state : FSMContext):
    contact_data = message.text

    if len(contact_data) > 1024:
        return await message.reply("Слишком длинное сообщение")

    data = await state.get_data()

    send_text = "Спасибо ваша заявка принята."

    await message.answer(send_text)

    message_content = await get_welcome_message()
    send_video = message_content["video"]
    send_text = message_content["text"]
    main_menu_kb = message_content["keyboard"]
    await message.answer_video(caption=send_text, video=send_video, reply_markup=main_menu_kb)
    #await message.answer(send_text, reply_markup=main_menu_kb)
    


    await state.set_state(UserStates.MAIN_MENU)


    send_text = f"""
<b>Пробник</b>
<b>Пользователь:</b> @{message.from_user.username}
<b>ЖК:</b> <i>{data["rc"]}</i>
<b>Дата получения:</b> <code>{data["sample_datetime"]}</code>

<b>Контактные данные:</b>
<i>{contact_data}</i>"""
    
    await bot.send_message(chat_id=SEND_ORDER_CHAT_ID, text = send_text)

    edit_contact_data(user_id=message.from_user.id, contact_data=message.text)
    change_get_sample(user_id=message.from_user.id)






@router.callback_query(F.data == "make_order", UserStates.MAIN_MENU)
async def make_order(call : CallbackQuery, state : FSMContext):
    contact_data = get_contact_data(call.from_user.id)
    if not contact_data:
        send_text = """Пожалуйста, напишите ваше имя и номер телефона для связи: 
Эта информация нужна, чтобы мы могли уточнить детали доставки.😊"""
        try:
            await call.message.edit_text(text = send_text)
            await state.set_state(UserStates.INPUT_CONTACT_DATA_ORDER)

        except TelegramBadRequest:
            await call.message.answer(text = send_text)
            await state.set_state(UserStates.INPUT_CONTACT_DATA_ORDER)
        
        except Exception as ex:
            logger.error(f"Error in make_order handler: {str(ex)}")
            await call.answer(text = "Произошла ошибка, попробуйте позже.")

        

        return
    
    send_text = "Спасибо ваша заявка принята."
    await call.message.reply(send_text)

    send_text = f"""
<b>Заказ</b>
<b>Пользователь:</b> @{call.from_user.username}

<b>Контактные данные:</b>
<i>{contact_data}</i>"""
    
    await bot.send_message(chat_id=SEND_ORDER_CHAT_ID, text = send_text)
    


@router.message(F.text, UserStates.INPUT_CONTACT_DATA_ORDER)
async def input_contact_data_order(message : Message, state : FSMContext):
    contact_data = message.text
    if len(contact_data) > 1024:
        return await message.reply("Слишком длинное сообщение")
    
    send_text = "Спасибо ваша заявка принята."
    await message.answer(send_text)
    message_content = await get_welcome_message()
    send_video = message_content["video"]
    send_text = message_content["text"]
    main_menu_kb = message_content["keyboard"]
    
    await message.answer_video(caption=send_text, video=send_video, reply_markup=main_menu_kb)
    #await message.answer(send_text, reply_markup=main_menu_kb)


    edit_contact_data(message.from_user.id, contact_data)

    send_text = f"""
<b>Заказ</b>
<b>Пользователь:</b> @{message.from_user.username}

<b>Контактные данные:</b>
<i>{contact_data}</i>"""
    
    await bot.send_message(chat_id=SEND_ORDER_CHAT_ID, text = send_text)







    