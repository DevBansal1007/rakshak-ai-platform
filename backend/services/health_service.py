from backend.config import settings


def get_health_status():
    return {
        "status": "running",
        "project": settings.APP_NAME,
        "version": settings.VERSION
    }