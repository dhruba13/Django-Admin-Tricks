gen = (a for a in range(6))

obj_1,obj_2,obj_3, *gen = gen
print(gen)  #[3, 4, 5] ! unpacked list, not work for infinity!!!

gen = (obj_1,obj_2,obj_3, *gen) # pack again in tuple
gen = (obj for obj in gen) # pack again in generator



def genreport(gen):
    return ((print(item), item)[-1] for item in gen)
# it can be logging.log


import itertools
def clone_generator(gen):
    first,  second = itertools.tee(gen, n=2)
    return first,  second
    # Return n independent iterators from a single iterable.



import more_itertools
def inspect_some_items(gen):
    firsts_n, iterator = more_itertools.spy(gen, n=1)
    return first_n, iterator
    # Return a 2-tuple with a first n elements of iterable, and an iterator
    #This allows you to “look ahead” at the items in the iterator.


def test_func(*args):
    return args

print(fun(1,2,3,4))  #(3, 4, 5)

