# def permutation_generator(word):
#     for index, letter in enumerate(word):
#         yield ''.join((letter, *permutation_generator(word[:index] + word[index + 1:])))

def permutation_generator(word):
    for index, letter in enumerate(word):
        yield from (letter + n for n in permutation_generator(word[:index] + word[index + 1:]))
    else:
        yield ''

print('hello')
for x in permutation_generator("home"):
    print(x)


def fibonacci(limit):
    a, b = 0, 1
    index = 1  # the index of the fibonacci number 'b'
    while index < limit:
        goto = (yield b)
        if goto is None:
            goto = index + 1
        if goto > limit:
            break
        steps = goto - index
        if steps >= 0:
            for __ in range(steps):
                a, b = b, a + b
        else:
            for __ in range(-steps):
                a, b = b - a, a
        index = goto