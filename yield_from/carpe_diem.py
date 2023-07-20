
while True: # infinity generator
    if something:
        break
    ...  # skipped on break

INFINITY = (_ for _ in iter(int, 1))
for __moment__ in INFINITY:
    if something:
        INFINITY.clean()
    ...  # Carpe diem


# Stoppable:
clean = False
iterator = iter(lambda: clean, not clean)

for iteration in iterator:
    ... # do something
    if  some_cause:
        clean = True
    ... # do something else
    if  other_cause:
        break
    ... # do something at the end of loop
else:
    # some finally code

