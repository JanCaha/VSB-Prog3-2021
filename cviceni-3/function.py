from typing import List


def add_to_element_of_list(list_of_values: List[float], value_to_add: float) -> List[float]:
    """
    This function adds value_to_add to every element of list_of_values.

    Parameters
    ----------
    list_of_values: List[float]
        List of values.

    value_to_add: float
        Value to add to every element of the list.

    Returns
    -------
    List[float]
        Some text.
    """

    if (not isinstance(value_to_add, (int, float))) or isinstance(value_to_add, bool):
        raise ValueError("`value_to_add` must be either `int` or `float`. It is `{}`.".format(type(value_to_add)))

    return_list = []

    for val in list_of_values:
        return_list.append(val + value_to_add)

    # return_list.append(value_to_add)

    return return_list
