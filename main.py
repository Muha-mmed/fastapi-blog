from fastapi import FastAPI
from blog.routes import router

app =FastAPI()

app.include_router(router)