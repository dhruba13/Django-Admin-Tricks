import time
import asyncio

from europython2023.curio_async import REPORT

def count(idx):
    print(f'One{idx}')
    time.sleep(1)
    print(f'Two{idx}')

def main():
    count(1)
    count(2)
    count(3)

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)
