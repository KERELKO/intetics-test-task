from pathlib import Path
import aiocsv
import csv
import aiofiles  # type: ignore[import-untyped]

from app.types import QuestionAnswer


class CSVStorage:
    """File-based storage. Provides common operations on data:
    * save_entry - save new question-answer to file
    * read_entries - read all entries from file and load it in memory
    * get_entries_by_user - load all entries in memory and return only associated with user
    """

    def __init__(self, file: Path):
        self.file = file
        if self.file.exists() is False:
            self._write_initial_row()

    def _write_initial_row(self):
        with open(self.file, 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['question', 'answer', 'user_id'])

    async def save_entry(self, qa: QuestionAnswer):
        async with aiofiles.open(self.file, 'a', newline='') as file:
            csv_writer = aiocsv.AsyncWriter(file)
            await csv_writer.writerow([qa['question'], qa['answer'], qa['user_id']])

    async def read_entries(self) -> list[QuestionAnswer]:
        result = []
        async with aiofiles.open(self.file, mode='r') as file:
            reader = aiocsv.AsyncDictReader(file)
            async for row in reader:
                result.append(QuestionAnswer(
                    question=row['question'], answer=row['answer'], user_id=int(row['user_id']),
                ))
        return result

    async def get_entries_by_user(self, user_id: int) -> list[QuestionAnswer]:
        result = []
        async with aiofiles.open(self.file) as file:
            reader = aiocsv.AsyncDictReader(file)
            async for row in reader:
                if int(row['user_id']) != user_id:
                    continue
                result.append(QuestionAnswer(
                    question=row['question'], answer=row['answer'], user_id=user_id,
                ))
        return result
