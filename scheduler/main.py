from apscheduler.schedulers.asyncio import AsyncIOScheduler

from importantFiles.config import data_base_path


scheduler = AsyncIOScheduler(
{
    
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///' + data_base_path
    }
}, timezone="Europe/Moscow",)