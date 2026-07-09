from fastapi import FastAPI
from backend.routes.health import router as health_router
from backend.config import settings
from backend.exceptions.handlers import global_exception_handler

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.add_exception_handler(Exception, global_exception_handler)
app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Rakshak AI"
    }