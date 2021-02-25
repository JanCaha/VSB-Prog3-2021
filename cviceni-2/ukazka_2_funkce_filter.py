import random


def even_number(x):
    return (x % 2) == 0


l = [1, 2, 3, 4, 5, 6]

r = filter(even_number, l)

print(r)
print(type(r))

r = list(r)

print(r)

l_long = [int(random.random() * 100) for x in range(0, 100)]

print(l_long)

r = list(filter(even_number, l_long))

print("-" * 60)
print(len(r))
print(r)
