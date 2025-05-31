import csv
from pathlib import Path
import aiofiles  # type: ignore[import-untyped]


class CSVStorage:
    def __init__(self, file: Path):
        self.file = file
        if self.file.exists() is False:
            self._write_initial_row()

    def _write_initial_row(self):
        with open(self.file, 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['question', 'answer'])

    async def save_entry(self, question: str, answer: str):
        async with aiofiles.open(self.file, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            await csv_writer.writerow([question, answer])

    async def read_entries(self) -> dict[str, str]:
        result = {}
        with open(self.file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                result[row['question']] = row['answer']
        return result
