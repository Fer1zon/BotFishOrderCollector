from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime, timedelta, time
from handlers.keyboard import in_menu
from importantFiles.database.models import Fish



def select_weekday(current_time : datetime) -> bool:
    if int(current_time.isoweekday()) == 3:
        return True
    elif int(current_time.hour) < 17 and int(current_time.isoweekday()) <= 4:
        return True
            

    return False
    

def get_datetime_order_kb(current_time : datetime = None) -> InlineKeyboardMarkup:    
    if not current_time:
        current_time = datetime.now()
    result = select_weekday(current_time)

    required_date_thursday = None
    required_date_friday = None

    if result and (current_time.isoweekday() == 3 or current_time.isoweekday() == 4):
        if current_time.isoweekday() == 3:
            required_date_friday = current_time + timedelta(days=2)

        elif current_time.isoweekday() == 4:
            required_date_friday = current_time + timedelta(days=1)

        required_date_friday = datetime.combine(required_date_friday, time(hour=20, minute=0))
    elif select_weekday(current_time):
        
        required_date_thursday = current_time
        required_date_friday = current_time + timedelta(days=1)
        

        for _ in range(7):
            if required_date_thursday.isoweekday() == 4:
                break

            required_date_thursday += timedelta(days=1)
            required_date_friday += timedelta(days=1)

        required_date_thursday = datetime.combine(required_date_thursday, time(hour=20, minute=0))
        required_date_friday = datetime.combine(required_date_friday, time(hour=20, minute=0))

        
        
    
    else:
        if current_time.isoweekday() == 3:
            required_date_thursday = current_time + timedelta(days=8)
        elif current_time.isoweekday() == 4:
            required_date_thursday = current_time + timedelta(days=7)
        elif current_time.isoweekday() == 5:
            required_date_thursday = current_time + timedelta(days=6)
        elif current_time.isoweekday() == 6:
            required_date_thursday = current_time + timedelta(days=5)
        elif current_time.isoweekday() == 7:
            required_date_thursday = current_time + timedelta(days=4)
        


        
        required_date_friday = required_date_thursday + timedelta(days=1)


        required_date_thursday = datetime.combine(required_date_thursday, time(hour=20, minute=0))
        required_date_friday = datetime.combine(required_date_friday, time(hour=20, minute=0))

    keyboard = InlineKeyboardBuilder()
    if not required_date_thursday:
        button2 = InlineKeyboardButton(text = f"Пятница {required_date_friday.strftime('%d.%m')} 18:00-22:00", callback_data=str(required_date_friday.strftime('%d.%m.%Y')) + ' ' + "ПТ")
        keyboard.add(button2).adjust(1)

    else:

        button1 = InlineKeyboardButton(text = f"Четверг {required_date_thursday.strftime('%d.%m')} 18:00-22:00", callback_data=str(required_date_thursday.strftime('%d.%m.%Y')) + ' ' + "ЧТ")
        button2 = InlineKeyboardButton(text = f"Пятница {required_date_friday.strftime('%d.%m')} 18:00-22:00", callback_data=str(required_date_friday.strftime('%d.%m.%Y')) + ' ' + "ПТ")
        keyboard.add(button1, button2).adjust(1)
    
    
    return keyboard.as_markup()


async def make_fish_products_keyboard(fish : list[Fish]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for item in fish:
        
        keyboard.add(InlineKeyboardButton(text = str(item.title), callback_data=str(item.id)))

    return keyboard.adjust(1).as_markup()






        


