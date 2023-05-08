import time

FILE_BASE, *__ = __file__.rpartition('\\')

def read(filename, idx):
    print('started', filename, idx)
    with open(filename, 'rb') as file:
        try:
            return file.readlines()
        finally:
            print('readed', filename, idx)


def main():
    tasks = []

    for idx, filename in enumerate(('pg.pdf', 'curi.py', 'afile.py', 'async.py')):
        tasks.append((filename, read(f'{FILE_BASE}\\{filename}', idx)))

    for idx, task in enumerate(tasks, 1):
        ...

    print(idx, 'read completed.')


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.5f} seconds.")