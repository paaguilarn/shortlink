from fastapi import FastAPI

from core.config import settings


def get_app() -> FastAPI:
    server = FastAPI(
        title=settings.project_name,
        openapi_url=settings.openapi_route,
        debug=settings.debug,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
    )

    return server
