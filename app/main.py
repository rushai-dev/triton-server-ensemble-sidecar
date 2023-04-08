from utils.app_exceptions import AppExceptionCase
from fastapi import FastAPI

from routers import inference

from utils.app_exceptions import app_exception_handler


app = FastAPI()

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)
    
app.include_router(inference.router)