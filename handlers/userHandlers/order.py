from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from importantFiles.FSM import UserStates
import logging

from utils.message_making import make_order as make_order_message, get_welcome_message, order_ready as order_ready_message, make_order_message_for_admin

from aiogram.exceptions import TelegramBadRequest
from importantFiles.config import SEND_ORDER_CHAT_ID, bot

from utils.database_working import check_items_exists, get_products, check_product, add_product_to_basket, clear_basket, get_product

from utils.keyboard_maker import get_datetime_order_kb, make_fish_products_keyboard

from handlers.keyboard import choice_fish_type_kb, making_order
from datetime import datetime




router = Router()
logger = logging.getLogger(__name__)




@router.callback_query(F.data == "make_order", UserStates.MAIN_MENU)
async def make_order(call : CallbackQuery, state : FSMContext):

    result = await check_items_exists()
    if not result:
        return await call.message.reply("Пока что каталог пуст")
    content = await make_order_message()

    try:
        await call.message.edit_text(text = content["text"], reply_markup=content["keyboard"])
        await state.set_state(UserStates.CHOICE_RESIDENTIAL_COMPLEX_ORDER)

    except TelegramBadRequest:
        await call.message.answer(text = content["text"], reply_markup=content["keyboard"])
        await state.set_state(UserStates.CHOICE_RESIDENTIAL_COMPLEX_ORDER)
    
    except Exception as ex:
        logger.error(f"Error in make_order handler: {str(ex)}")
        await call.answer(text = "Произошла ошибка, попробуйте позже.")




@router.callback_query(F.data.in_({"НОВЫЙ ЛЕССНЕР", "FAMILIA", "АРИОСТО", "ГРАНД ВЬЮ"}), UserStates.CHOICE_RESIDENTIAL_COMPLEX_ORDER)
async def choice_residential_complex(call : CallbackQuery, state : FSMContext):
    keyboard  = get_datetime_order_kb()
    send_text = "Выберите время доставки"

    await call.message.answer(send_text, reply_markup=keyboard)
    await state.set_state(UserStates.CHOICE_TIME_DELIVERY_ORDER)

    await state.update_data(rc=call.data)


@router.callback_query(F.data.not_in({"in_menu"}), UserStates.CHOICE_TIME_DELIVERY_ORDER)
async def choice_time_delivery(call : CallbackQuery, state :FSMContext):
    await state.update_data(delivery_time = call.data)

    send_text = """Выбор вида рыбы"""

    await call.message.answer(send_text, reply_markup=choice_fish_type_kb)
    await state.set_state(UserStates.CHOICE_FISH_TYPE_ORDER)


@router.callback_query(F.data.in_({"Лосось", "Форель"}), UserStates.CHOICE_FISH_TYPE_ORDER)
async def choice_fish_type(call : CallbackQuery, state : FSMContext):
    result = await check_items_exists(type_ = call.data)
    if not result:
        return await call.answer(f"{call.data} отсутствует!")
    
    products = await get_products(type_ = call.data)
    keyboard = await make_fish_products_keyboard(products)

    await call.message.answer(call.data, reply_markup=keyboard)
    await state.set_state(UserStates.CHOICE_PRODUCT_ORDER)



@router.callback_query(F.data, UserStates.CHOICE_PRODUCT_ORDER)
async def choice_product(call : CallbackQuery, state : FSMContext):
    result = await check_product(id = call.data)
    if not result:
        await call.answer("Такой позиции не существует!")

    await state.update_data(product_id = call.data)
    product_title = await get_product(call.data)
    product_title = product_title.title
    send_text = f"{product_title} - введите количество штук"

    await call.message.answer(send_text)
    await state.set_state(UserStates.INPUT_COUNT_PRODUCT_ORDER)


@router.message(F.text, UserStates.INPUT_COUNT_PRODUCT_ORDER)
async def input_count_product(message : Message, state : FSMContext):
    try:
        count = float(message.text)
        if count <= 0:
            send_text = "Число не должно быть меньше 0!"
            return await message.answer(send_text)
        
    except ValueError:
        send_text = "Введенное вами значение не число!"
        return await message.answer(send_text)
    
    state_data = await state.get_data()
    product_id = state_data["product_id"]

    await add_product_to_basket(product_id, message.from_user.id, count)

    send_text = "Что то еще или оформить?"
    await message.answer(send_text, reply_markup=making_order)

@router.callback_query(F.data == "Ещё", UserStates.INPUT_COUNT_PRODUCT_ORDER)
async def yes_continue(call : CallbackQuery, state : FSMContext):
    send_text = """Выбор вида рыбы"""

    await call.message.answer(send_text, reply_markup=choice_fish_type_kb)
    await state.set_state(UserStates.CHOICE_FISH_TYPE_ORDER)


@router.callback_query(F.data == "Оформить", UserStates.INPUT_COUNT_PRODUCT_ORDER)
async def place_an_order(call : CallbackQuery, state :FSMContext):
    send_text = await order_ready_message(call.from_user.id)

    await call.message.answer(send_text)
    await state.set_state(UserStates.INPUT_CONTACT_DATA_ORDER)




    

    


@router.message(F.text, UserStates.INPUT_CONTACT_DATA_ORDER)
async def input_contact_data_order(message : Message, state : FSMContext):
    contact_data = message.text
    if len(contact_data) > 1024:
        return await message.reply("Слишком длинное сообщение")
    
    send_text = "Спасибо. Ваш заказ принят!!!"
    await message.answer(send_text)
    message_content = await get_welcome_message()
    send_video = message_content["video"]
    send_text = message_content["text"]
    main_menu_kb = message_content["keyboard"]
    
    await message.answer_video(caption=send_text, video=send_video, reply_markup=main_menu_kb)
    await state.set_state(UserStates.MAIN_MENU)
    
    #await message.answer(send_text, reply_markup=main_menu_kb)


    
    state_data = await state.get_data()
    send_text = await make_order_message_for_admin(message.from_user.id, contact_data, message.from_user.username, state_data["rc"], state_data["delivery_time"] )
    
    await bot.send_message(chat_id=SEND_ORDER_CHAT_ID, text = send_text)

    await clear_basket(message.from_user.id)