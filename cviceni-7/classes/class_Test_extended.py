import numpy as np
import random
from .class_Test import TestClass


class TestClassExt(TestClass):

    multiply_const = 100

    def __init__(self, number_of_elements: int):

        super().__init__(0)

        self.values = []

        self._min = None
        self._max = None

        for i in range(number_of_elements):
            self.values.append(random.random() * self.multiply_const)

    def __repr__(self):
        return F"TestClassExt with {len(self.values)} elements."

    def sum(self) -> float:
        return np.sum(self.values)

    def _calculate_sum(self) -> float:
        sum = 0
        for i in range(len(self.values)):
            sum += self.values[i]
        return sum

    @property
    def maximum(self) -> float:
        if self._max:
            return self._max
        else:
            self._max = np.amax(self.values)
            return self._max

    @property
    def minimum(self) -> float:
        if not self._min:
            self._min = np.amin(self.values)

        return self._min
