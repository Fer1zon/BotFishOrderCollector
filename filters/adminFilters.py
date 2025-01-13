from aiogram.filters import Filter
from importantFiles.config import admins
from aiogram.types import Message, CallbackQuery



class IsAdmin(Filter):
    def __init__(self):
        self.admin_id = admins

    async def __call__(self, message : Message | CallbackQuery):
        return message.from_user.id in self.admin_id
        

    