import csv
from pathlib import Path

import aiofiles  # type: ignore[import-untyped]

from app.types import QuestionAnswer


class CSVStorage:
    def __init__(self, file: Path):
        self.file = file
        if self.file.exists() is False:
            self._write_initial_row()

    def _write_initial_row(self):
        with open(self.file, 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['question', 'answer'])

    async def save_entry(self, qa: QuestionAnswer):
        async with aiofiles.open(self.file, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            await csv_writer.writerow([qa['question'], qa['answer']])

    async def read_entries(self) -> list[QuestionAnswer]:
        result = []
        with open(self.file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                result.append(QuestionAnswer(question=row['question'], answer=row['answer']))
        return result
