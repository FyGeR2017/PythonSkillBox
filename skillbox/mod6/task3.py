from math import log10


def armstrong_numbers():
    n = 100

    while True:

        order = int(log10(n)) + 1
        digs = [int(d) for d in str(n)]

        if sum(d ** order for d in digs) == n:
            yield n

        n += 1


generator = armstrong_numbers()


def get_armstrong():
    return next(generator)


for _ in range(8):
    print(get_armstrong(), end=' ')
