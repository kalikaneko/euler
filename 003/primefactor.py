import math


def is_prime(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return x > 1


def factors(x):
    yield 1
    for i in xrange(2, int(math.sqrt(x))):
        if x % i == 0:
            yield i
            yield x/i
    yield x

print max(filter(is_prime, factors(600851475143)))
