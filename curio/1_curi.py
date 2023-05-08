import time
import curio

from europython2023.curio import REPORT

async def count(variable):
    print(f'One{variable}')
    await curio.sleep(1)
    print(f'Two{variable}')

async def main():
    counter1 = await curio.spawn(count, 1)
    counter2 = await curio.spawn(count, 2)
    counter3 = await curio.spawn(count, 3)
    await counter3.join()
    await counter1.join()
    await counter2.join()

if __name__ == "__main__":
    s = time.perf_counter()
    curio.run(main())
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)
