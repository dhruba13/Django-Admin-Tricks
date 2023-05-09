import time
import asyncio

from europython2023.curio_async import REPORT

async def count(variable):
    print(f'One{variable}')
    await asyncio.sleep(1)
    print(f'Two{variable}')

async def main():
    counter1 = asyncio.create_task(count(1))
    counter2 = asyncio.create_task(count(2))
    counter3 = asyncio.create_task(count(3))
    await counter3
    await counter1
    await counter2

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)