a = [1, 2, 3]  # some iterable with many ierables
b = (iter('q'), iter('w'))  # other iterable with many ierables
c = iter(iter([...])) # other iterable

def example_1(*iterables):
    try:
        iterators = [iter(iterable) for iterable in iterables]
        while iterators:
            yield (next(iterator) for iterator in iterators)
    except Exception as internal_err:
        print('you can not see', internal_err) # i can not catch it here


try:
    for step in example_1(a,b,c):
        print(list(step))  # i can catch it here
except Exception as global_err:
    # or i can catch it here
    print('here you can see ', global_err)
