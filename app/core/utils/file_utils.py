import csv
from typing import Dict

import aiofiles


async def load_csv(file_path: str) -> Dict[str, str]:
    result = {}
    async with aiofiles.open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        async for row in csv_reader:
            if len(row) >= 2:
                result[row[0]] = row[1]
    return result

async def load_markdown(file_path: str) -> str:
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
    return content
