INFINITY = iter(int, 1)  # infinity generator

for __moment__ in INFINITY:
    ...  # Carpe diem


# Stoppable:
clean = False
iterator = iter(lambda: clean, not clean)

for iteration in iterator:
    ... # do something
    if  some_cause:
        clean = True
    ... # do something
    if  other_cause:
        break
else:
    # some code

