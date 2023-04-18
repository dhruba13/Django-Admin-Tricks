def zip(*iterables):  # docs.python.org/3.3/library/functions.html#zip
    """Call zip('ABCD', 'xy') --> Ax By."""
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []  # result = (next(iterator) for iterator in iterators)
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


def better_zip(*iterables):
    iterators = [iter(iterable) for iterable in iterables]
    while iterators:
        yield (next(iterator) for iterator in iterators)

# finally

def my_zip(*args):
    yield from ((next(arg) for arg in gen)
        for gen in iter([iter(arg) for arg in args].__iter__, None))

# finally again

def collect(iterators):
    for iterator in iterators:
        try:
            yield next(iterator)
        except StopIteration:
            break

def my_zip(*args):
    yield from (collect(gen)
        for gen in iter([iter(arg) for arg in args].__iter__, None))



a = [1,2,3,4,5,6]
b = ['q','w','e','r']
try:
    print('i am in main before')
    for step in (step for step in my_zip(a,b) if step is not None):
        print(list(step))
except Exception as e:
    print('i am in main', e)
    ...



try:
    print('i am in main before')
    for step in better_zip(a,b):
        print(list(step))
except Exception as e:
    print('i am in main', e)
    ...

#  from yield_from.my_zip import better_zip, my_zip
#> for arr in better_zip( (1,'w', 4, 9), (5,5,5) ):
#...     print(tuple(arr))

# def my_zip(*iterables):
#     try:
#         yield from (next(iterator) for iterator in [iter(iterable) for iterable in iterables])
#     except RuntimeError:
#         # we can check RuntimeError.__cause__ = StopIteration
#         return
