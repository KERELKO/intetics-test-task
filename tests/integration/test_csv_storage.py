from pathlib import Path
import pytest

from app.types import QuestionAnswer
from app.storages.csv import CSVStorage


TEST_CSV_STORAGE_FILE_PATH = Path(__file__).parent / 'test_storage.csv'


@pytest.mark.asyncio
async def test_csv_storage():
    try:
        storage = CSVStorage(TEST_CSV_STORAGE_FILE_PATH)

        qa = QuestionAnswer(
            question="How good is today's weather?", answer="It's sunny today!", user_id=1
        )

        empty_entries = await storage.read_entries()
        assert len(empty_entries) == 0

        await storage.save_entry(qa)

        entries = await storage.read_entries()
        assert len(entries) == 1

        entries_by_user = await storage.get_entries_by_user(user_id=1)

        assert len(entries_by_user) == 1
        assert entries_by_user[0]['user_id'] == 1

        assert storage
    finally:
        TEST_CSV_STORAGE_FILE_PATH.unlink()
