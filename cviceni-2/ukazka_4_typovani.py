def add(x, y):
    return x + y


def add_typed(x: float, y: float) -> float:

    if not isinstance(x, (float, int)):
        raise TypeError("`x` must be float. It is `{}`.".format(type(x)))

    if not isinstance(y, (float, int)):
        raise TypeError(F"`y` must be float. It is `{type(y)}`.")

    return x + y


print(add(1, 2))
print(add("první část textu", "druhá část textu"))
# print(add(1, "druhá část textu"))

print(add_typed(1, 5))
print(add_typed(2.0, "druhá část textu 123648"))
print(add_typed("první část textu", "druhá část textu 123648"))
