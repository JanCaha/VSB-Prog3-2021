import random
import numpy as np


class TestClass:

    multiply_const = 1000

    def __init__(self, number_of_elements: int):

        self.values = self.generate_random_values(number_of_elements, self.multiply_const)

        self._range = None

    def __repr__(self):
        return F"TestClass with {len(self.values)} elements."

    @property
    def maximum(self):
        return np.amax(self.values)

    @property
    def minimum(self):
        return np.amin(self.values)

    @property
    def range(self):
        if self._range:
            return self._range
        else:
            self._range = self.maximum - self.minimum
            return self._range

    def new_random_values(self, number_of_elements: int):

        self._range = None
        self.values = self.generate_random_values(number_of_elements, self.multiply_const)

    def __gt__(self, other):
        if isinstance(other, TestClass):
            return self.maximum > other.maximum
        else:
            raise NotImplementedError(F"Cannot compare TestClass to {type(other)}.")

    def __lt__(self, other):
        if isinstance(other, TestClass):
            return self.minimum < other.minimum
        else:
            raise NotImplementedError(F"Cannot compare TestClass to {type(other)}.")

    @staticmethod
    def generate_random_values(number_of_elements: int, multiply_const: float) -> list[float]:

        values = []

        for i in range(number_of_elements):
            values.append(random.random() * multiply_const)

        return values
