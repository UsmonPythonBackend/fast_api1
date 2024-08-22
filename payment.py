import asyncio

from fastapi import APIRouter

payment_router = APIRouter(prefix="/payment", tags=["payment"])

# async def generic():
#     data = 1
#     for i in range(1, 12133):
#         data += i
#     return data

async def generic():
    global product
    product += 1
    print(f"Xozirgi xolat: {product}")
    await asyncio.sleep(0.1)

@payment_router.get("/")
async def payment():
    data = await generic()
    return {"data": data}
