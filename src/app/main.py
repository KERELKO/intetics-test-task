from fastapi import FastAPI

from .api.handlers import router as ai_router


def fastapi_app_factory() -> FastAPI:
    app = FastAPI()

    app.include_router(router=ai_router, prefix='/api')

    return app
