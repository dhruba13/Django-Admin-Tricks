from pathlib import Path

COUNT = 1
FILE_BASE = Path(__file__).parent
# FILE_LIST = (FILE_BASE / 'docs' / 'pg.pdf', FILE_BASE / '1_curi.py', FILE_BASE / '1_tri.py', FILE_BASE / '1_async.py') * COUNT
FILE_LIST = (FILE_BASE / '1_curi.py', FILE_BASE / '1_tri.py', FILE_BASE / '1_async.py') * COUNT

HEADERS = b'HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
BODY = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>Hi</body></html>'


def REPORT(file, *args, **kwargs):
    return ''
    print(f'{file} executed in {args[0]:0.5f} seconds.')


# import shutil

# FILE_LIST = [FILE_BASE / 'examples' / f'pg{i}.pdf' for i in range(COUNT)]

# def generate_files():
#     base = FILE_BASE / 'docs' / 'pg.pdf'

#     Path.mkdir(FILE_BASE / 'examples', exist_ok=True)
#     for name in FILE_LIST:
#         shutil.copy(base, name)

# if __name__ == '__main__':
#     generate_files()
