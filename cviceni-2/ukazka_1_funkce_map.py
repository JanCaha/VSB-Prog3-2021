import random


def power2(x):
    return x ** 2


l = [1, 2, 3, 4, 5]

r = map(power2, l)

print(r)
print(type(r))

r = list(r)

print(r)

l_long = [int(random.random() * 100) for x in range(0, 1000)]

print(l_long)

r = list(map(power2, l_long))

print(r)
