from pathlib import Path
import pytest

from app.storages.csv import CSVStorage


TEST_CSV_STORAGE_FILE_PATH = Path(__file__).parent / 'test_storage.csv'


@pytest.mark.asyncio
async def test_csv_storage():
    storage = CSVStorage(TEST_CSV_STORAGE_FILE_PATH)
    assert storage
