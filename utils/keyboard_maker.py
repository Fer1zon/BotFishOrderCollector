from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime, timedelta, time
from handlers.keyboard import in_menu



def select_weekday(current_time : datetime) -> bool:
    if int(current_time.isoweekday()) < 3:
        return True
    elif int(current_time.hour) < 17 and int(current_time.isoweekday()) <= 3:
        return True
            

    return False
    

def get_datetime_order_kb(current_time : datetime = None) -> InlineKeyboardMarkup:    
    if not current_time:
        current_time = datetime.now()
    if select_weekday(current_time):
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

    
    button1 = InlineKeyboardButton(text = f"{required_date_thursday.strftime('%d.%m')} 18:00-22:00", callback_data=str(required_date_thursday.strftime('%d.%m.%Y')))
    button2 = InlineKeyboardButton(text = f"{required_date_friday.strftime('%d.%m')} 18:00-22:00", callback_data=str(required_date_friday.strftime('%d.%m.%Y')))
    keyboard = InlineKeyboardBuilder().add(button1, button2).adjust(1).as_markup()

    return keyboard


        


