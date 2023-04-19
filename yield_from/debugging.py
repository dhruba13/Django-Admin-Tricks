

def genreport(gen):
    return ((print(item), item)[-1] for item in gen)
# it can be logging.log


import itertools
first,  second = itertools.tee(iterable, n=2)
# Return n independent iterators from a single iterable.



import more_itertools:
firsts_n, iterator = more_itertools.spy(iterable, n=1)
# Return a 2-tuple with a first n elements of iterable, and an iterator
#This allows you to “look ahead” at the items in the iterator.
