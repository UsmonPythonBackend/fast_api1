from fastapi import FastAPI
from auth import login_router
from payment import payment_router
from cargo import cargo_router
from store import store_router


app = FastAPI()
app.include_router(login_router)
app.include_router(payment_router)
app.include_router(cargo_router)
app.include_router(store_router)

@app.get("/")
async def home():
    return {"message": "home page"}

@app.get("/about")
async def about():
    return {"message": "about page"}