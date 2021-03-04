import unittest

from function import add_to_element_of_list


class TestsForFunction(unittest.TestCase):

    def test_case_a(self):

        r = add_to_element_of_list([1, 2, 3], 1)

        self.assertIsInstance(r, list)

        self.assertEqual(len(r), 3)

        self.assertListEqual(r, [2, 3, 4])

    def test_case_b(self):

        with self.assertRaisesRegex(ValueError, "`value_to_add` must be either `int` or `float`"):
            r = add_to_element_of_list([1, 2, 3], "text")

        with self.assertRaises(ValueError):
            r = add_to_element_of_list([1, 2, 3], True)
