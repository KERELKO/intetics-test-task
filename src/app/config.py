from dataclasses import dataclass
from functools import cache
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class Config:
    deepseek_api_key: str = os.getenv('DEEPSEEK_API_KEY', '')
    csv_file_path: str = os.getenv('CSV_FILE_PATH', '')


@cache
def get_config() -> Config:
    return Config()
