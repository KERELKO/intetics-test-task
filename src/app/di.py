from pathlib import Path
from typing import Annotated

from fastapi import Depends

from app.clients.ai import ChatGPT
from app.config import Config, get_config
from app.services import EmbeddingService
from app.storages.csv import CSVStorage

ConfigDep = Annotated[Config, Depends(get_config)]


def ai_client(config: ConfigDep) -> ChatGPT:
    return ChatGPT(api_key=config.openai_api_key)


def storage(config: ConfigDep) -> CSVStorage:
    return CSVStorage(Path(config.csv_file_path))


def embedding_service() -> EmbeddingService:
    return EmbeddingService(model='text-embedding-ada-002')


AIClientDep = Annotated[ChatGPT, Depends(ai_client)]
StorageDep = Annotated[CSVStorage, Depends(storage)]
EmbeddingServiceDep = Annotated[EmbeddingService, Depends(embedding_service)]
