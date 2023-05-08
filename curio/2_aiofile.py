import asyncio
import time
import aiofiles

from europython2023.curio import FILE_LIST, FILE_BASE, REPORT

async def read(filename, idx):
    print('started', filename, idx)
    async with aiofiles.open(f'{filename}', mode='r') as file:
        try:
            return (await file.read(), idx)
        finally:
            print('readed', filename, idx)


async def main():
    tasks = []
    # Iterate through files in the directory.
    for idx, filename in enumerate(FILE_LIST):
        tasks.append(asyncio.create_task(read(f'{FILE_BASE}\\{filename}', idx)))

    response = await asyncio.gather(*tasks, return_exceptions=True)
    idx = 0
    for task in response:
        idx += 1

    print(idx, 'completed.')


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)
