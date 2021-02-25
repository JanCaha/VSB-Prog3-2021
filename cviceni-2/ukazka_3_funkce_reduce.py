from functools import reduce


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


l = [20, 1, 2, 3, 4, 5, 6]

r = reduce(minus, l)

print(type(r))
print(r)

# zápis cyklem

result = l[0]

for i in range(1, len(l)):
    result = minus(result, l[i])

print(result)
