from importantFiles.config import new_session
from importantFiles.database.models import User

from sqlalchemy import select



async def check_user(user_id : int):
    async with new_session() as session:
        query = select(User.user_id).where(User.user_id == user_id)
        result = await session.execute(query)

        if result.first():
            return True
        
        return False
    
async def add_user(user_id : int, username : str):
    if await check_user(user_id):
        return False
    
    async with new_session() as session:
        newUser = User(user_id = user_id, name = username)

        session.add(newUser)

        await session.commit()
        return True
