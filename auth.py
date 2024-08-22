#login, register, password_reset va password_confermation
from fastapi import APIRouter

login_router = APIRouter(prefix="/auth", tags=["auth"])



@login_router.get('/login')
async def login():
    return {"message": "login page"}


@login_router.get('/register')
async def success():
    return {"message": "register successfully"}


@login_router.get('/password_reset')
async def password_reset():
    return {"message": "password reset"}


@login_router.get('/password_confermation')
async def password_confermation():
    return {"message": "password confermation"}