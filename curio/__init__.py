FILE_BASE, *__ = __file__.rpartition('\\')

FILE_LIST = ('docs\\pg.pdf', '1_curi.py', '1_tri.py', '1_async.py')

def REPORT(file, elapsed):
    print(f'{file} executed in {elapsed:0.2f} seconds.')
