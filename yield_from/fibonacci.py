# recurcive function
def fibonacci_list(n):
    if n < 2:
        return 0, 1
    if n < 3:
        return 1, 1
    if n > 2:
        a, b = fibonacci_list(n-1)
        return b, b + a

# recurcive generator
def fibonacci_generator(n):
    if n < 2:
        yield 0, 1
    elif n < 3:
        yield 1, 1
    elif n > 2:
        (a, b), *_ = fibonacci_generator(n-1)
        yield b, a + b


from time import perf_counter_ns

def check():
    time = perf_counter_ns()
    a = fibonacci_list(900)
    print (perf_counter_ns()-time)

    time = perf_counter_ns()
    a = next(fibonacci_generator(900))
    print (perf_counter_ns()-time)