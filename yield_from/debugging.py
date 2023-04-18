We can wrap our generators to output data:
def genreport(gen):
    return ((print(item), item)[-1] for item in gen)
# it can be logging.log

We can use itertools.tee:
itertools.tee(iterable, n=2)
# Return n independent iterators from a single iterable.

We can use more_itertools.spy:
more_itertools.spy(iterable, n=1)
# Return a 2-tuple with a first n elements of iterable, and an iterator
#This allows you to “look ahead” at the items in the iterator.
