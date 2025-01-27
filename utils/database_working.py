from importantFiles.config import new_session
from importantFiles.database.models import Fish, Basket

from sqlalchemy import select, delete, func, update, insert





async def check_items_exists(type_ = None) -> bool:
    async with new_session() as session:

        if not type_:
            products = await session.scalars(select(Fish).limit(1))
            if products.first():
                return True 
            
            return False

        
        products = await session.scalars(select(Fish).where(Fish.type_ == type_).limit(1))
        if products.first():
            return True 
        
        return False



async def get_products(type_ : str) -> list[Fish]:
    async with new_session() as session:
        
        products = await session.scalars(select(Fish).where(Fish.type_ == type_))
        
        if not await check_items_exists(type_ = type_):
            return None
        
        return products 
    
async def get_product(id : int):
    async with new_session() as session:
        product = await session.scalar(select(Fish).where(Fish.id == id))
        return product
    

    

async def check_product(id : int) -> bool:
    async with new_session() as session:
        
        product = await session.scalars(select(Fish).where(Fish.id == id))
        
        if product.first():
            return True 
        
        return False
    
async def check_product_in_basket(id : int, user_id : int) -> bool:
    async with new_session() as session:
        
        product = await session.scalars(select(Basket).where(Basket.fish_id == id, Basket.user_id == user_id))
        
        if product.first():
            return True 
        
        return False
    

async def add_product_to_basket(fish_id : int, user_id : int, count_ : int):
    async with new_session() as session:
        result = await check_product_in_basket(id  = fish_id, user_id=user_id)
        title = await session.scalar(select(Fish.title).where(Fish.id == fish_id))
        
        if result:
            query = update(Basket).where(Basket.fish_id == fish_id, Basket.user_id == user_id).values(count = Basket.count + count_)
            await session.execute(query)

        else:
            query = insert(Basket).values(user_id = user_id, fish_id = fish_id, count = count_, title = title)
            await session.execute(query)
        
        await session.commit()

async def clear_basket(user_id : int):
    async with new_session() as session:
        query = delete(Basket).where(Basket.user_id == user_id)
        await session.execute(query)
        await session.commit()


async def get_basket_products(user_id : int) -> list[Fish]:
    async with new_session() as session:
        query = select(Basket).where(Basket.user_id == user_id)
        result = await session.scalars(query)

        return result
        




        
        
