#!/usr/env python
def fib(li, maxval):
    if li[-1] >= maxval:
        return li[:-1]
    return fib(li + [li[-1] + li[-2]], maxval)

print sum([x for x in fib([1, 2], 4000000) if x % 2 == 0])
