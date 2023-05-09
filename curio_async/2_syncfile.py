import time
from europython2023.curio_async import REPORT, FILE_LIST


def read(filename, idx):
    print('started', filename, idx)
    with open(filename, 'rb') as file:
        try:
            return file.readlines()
        finally:
            print('readed', filename, idx)


def main():
    tasks = []

    for idx, filename in enumerate(FILE_LIST):
        tasks.append((filename, read(f'{filename}', idx)))

    for idx, task in enumerate(tasks, 1):
        ...

    print(idx, 'read completed.')


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    REPORT(__file__, elapsed)
