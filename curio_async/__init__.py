from pathlib import Path

COUNT = 1
FILE_BASE = Path(__file__).parent
FILE_LIST = (FILE_BASE / 'docs' / 'pg.pdf', FILE_BASE / '1_curi.py', FILE_BASE / '1_tri.py', FILE_BASE / '1_async.py') * 1


def REPORT(file, elapsed):
    print(f'{file} executed in {elapsed:0.5f} seconds.')


# import shutil

# FILE_LIST = [FILE_BASE / 'examples' / f'pg{i}.pdf' for i in range(COUNT)]

# def generate_files():
#     base = FILE_BASE / 'docs' / 'pg.pdf'

#     Path.mkdir(FILE_BASE / 'examples', exist_ok=True)
#     for name in FILE_LIST:
#         shutil.copy(base, name)

# if __name__ == '__main__':
#     generate_files()
