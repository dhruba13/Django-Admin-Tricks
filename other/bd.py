from collections import Counter

from itertools import chain

def count_living_per_year(population):
    return Counter(chain(*(range(*bd) for bd in population)))

# At first: mix different types.

# type(count_living_per_year(...)) -> class 'collections.Counter'
# type({2000: 1, 2001: 2, 2002: 1}) -> class 'dict'

# At second, the representation of this objects is different:
# repr(count_living_per_year(...)) -> 'Counter({2001: 2, 2000: 1, 2002: 1})'
# repr({2000: 1, 2001: 2, 2002: 1}) -> '{2000: 1, 2001: 2, 2002: 1}'

def count_living_per_year_(population):
    return Counter(chain(*(range(*_) for _ in population)))


def coro(*args, **kwargs):
    print('strt coro')
    sended = yield 'result'
    print('strt coro')

async def acoro(*args, **kwargs):
    print('strt acoro')
    sended = await acoro('result')
    print('strt acoro')

def gen(*args, **kwargs):
    print('strt gen')
    sended =  acoro('result')
    for bit in 'resilt':
        yield bit
    print('end gen')


def yieldedcoro(*args, **kwargs):
    print('strt declaredcoro')
    sended = yield from gen()
    print('strt declaredcoro')


