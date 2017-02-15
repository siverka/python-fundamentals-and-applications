import itertools


def primes():
    x = 2
    while True:
        res = [x % i == 0 for i in range(2, x)]
        if not any(res):
            yield x
        x += 1


print(list(itertools.takewhile(lambda x : x <= 40, primes())))
