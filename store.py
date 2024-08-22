from fastapi import APIRouter

store_router = APIRouter(prefix="/store", tags=["store"])



@store_router.get('/new_items')
async def new_items():
    return {"message": "new_items"}


@store_router.get('/category')
async def category():
    return {"message": "category of products"}


@store_router.get('/discounts')
async def discounts():
    return {"message": "discounts"}