from functools import reduce

my_list = (el for el in range(100, 1001, 2))


def func(prev_el, el):
    return prev_el * el


print(reduce(func, my_list))
