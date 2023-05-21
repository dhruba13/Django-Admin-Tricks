import time
import curio
import aiofiles
import asyncio

from europython2023.curio_async import REPORT, FILE_LIST


async def read(filename, idx):
    # print(f'One {filename}')
    print('started', filename, idx)
    async with curio.file.aopen(filename, 'rb') as file:
        try:
            return await file.read()
        finally:
            print('readed', filename, idx)


async def main():
    async with curio.TaskGroup() as tasks:
        for idx, filename in enumerate(FILE_LIST):
            await tasks.spawn(read, f'{filename}', idx)
        idx = 0
        async for task in tasks:
            idx += 1

        print(idx, 'completed.')


if __name__ == "__main__":
    s = time.perf_counter()
    curio.run(main())
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)
