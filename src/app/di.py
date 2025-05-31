from typing import Annotated
from fastapi import Depends

from app.clients.ai import DeepSeek
from app.config import Config, get_config


ConfigDep = Annotated[Config, Depends(get_config)]


def ai_client(config: ConfigDep) -> DeepSeek:
    return DeepSeek(config.deepseek_api_key)


AIClientDep = Annotated[DeepSeek, Depends(ai_client)]
