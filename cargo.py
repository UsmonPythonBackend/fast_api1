# delivery, orders va order_story

from fastapi import APIRouter

cargo_router = APIRouter(prefix="/cargo", tags=["cargo"])




@cargo_router.get('/delivery')
async def delivery():
    return {"message": "Delivery page"}


@cargo_router.get('/orders')
async def orders():
    return {"message": "Orders"}


@cargo_router.get('/order_story')
async def order_story():
    return {"message": "order_story"}


