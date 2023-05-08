import time
import curio

FILE_BASE, *__ = __file__.rpartition('\\')


async def read(filename, idx):
    # print(f'One {filename}')
    print('started', filename, idx)
    async with curio.file.aopen(filename, 'rb') as file:
        try:
            return await file.readlines()
        finally:
            print('readed', filename, idx)

async def main():
    async with curio.TaskGroup() as tasks:
        for idx, filename in enumerate(('pg.pdf', 'curi.py', 'afile.py', 'async.py')):
            await tasks.spawn(read, f'{FILE_BASE}\\{filename}', idx)
        idx = 0
        async for task in tasks:
            idx += 1

        print(idx, 'completed.')

if __name__ == "__main__":
    s = time.perf_counter()
    curio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.5f} seconds.")
