from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.handlers import router as ai_router


def fastapi_app_factory() -> FastAPI:
    app = FastAPI()

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://localhost",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router=ai_router, prefix='/api')

    return app
