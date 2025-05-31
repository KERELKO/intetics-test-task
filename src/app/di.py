from pathlib import Path
from typing import Annotated

from fastapi import Depends

from app.clients.ai import DeepSeek
from app.config import Config, get_config
from app.storages.csv import CSVStorage

ConfigDep = Annotated[Config, Depends(get_config)]


def ai_client(config: ConfigDep) -> DeepSeek:
    return DeepSeek(config.deepseek_api_key)


def storage(config: ConfigDep) -> CSVStorage:
    return CSVStorage(Path(config.csv_file_path))


AIClientDep = Annotated[DeepSeek, Depends(ai_client)]
StorageDep = Annotated[CSVStorage, Depends(storage)]
