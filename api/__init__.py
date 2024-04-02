from fastapi import FastAPI

from api.endpoints import router
from core.config import settings
from events.usage_tracking_listener import setup_usage_tracking_handlers


def get_app() -> FastAPI:
    server = FastAPI(
        title=settings.project_name,
        openapi_url=settings.openapi_route,
        debug=settings.debug,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
    )

    server.include_router(router, prefix=settings.api_v1_route, tags=["URL"])

    setup_usage_tracking_handlers()

    return server
