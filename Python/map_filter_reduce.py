from functools import reduce
# MAP : passes an iterable in a function
def cube(x):
    return x**3

lst = [1, 2, 3, 4, 5, 6, 7]
new_lst = list(map(cube,lst))
print(new_lst)

# FILTER : filter the iterable based on predicate
def filter_ex(a):
    return a > 2
newest_lst = list(filter(filter_ex, lst))
print(newest_lst)

def sum(a,b):
    return a+b

Mysum = list(reduce(sum, lst))
print(Mysum)