import unittest

from mypythonpackage import fna

class fnaTests(unittest.TestCase):

    def test_string(self):

        self.assertIsInstance(fna(5), str)
