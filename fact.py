from functools import reduce
from math import factorial


def fact(n):
    my_list = (el for el in range(1, n + 1))

    def func(prev_el, el):
        return prev_el * el

    yield reduce(func, my_list)


print(factorial(13))
for el in fact(13):
    print(el)
