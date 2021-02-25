from typing import List, Union


def add(x: Union[float, int], y: Union[float, int]) -> Union[float, str, int]:
    return x + y


def add_to_list(l: List[float], x: Union[float, int]) -> List[float]:

    return_values = []

    for val in l:
        return_values.append(val + x)

    return return_values


print(add(1, 2))
print(add("první část textu", "druhá část textu"))

y = add_to_list(["str", "a", "b"], 1)

print(y)
