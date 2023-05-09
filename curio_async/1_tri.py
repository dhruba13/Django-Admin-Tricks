import time
import trio

from europython2023.curio_async import REPORT

async def count(variable):
    print(f'One{variable}')
    await trio.sleep(1)
    print(f'Two{variable}')

async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(count, 1)
        nursery.start_soon(count, 2)
        nursery.start_soon(count, 3)


if __name__ == "__main__":
    s = time.perf_counter()
    trio.run(main)
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)
