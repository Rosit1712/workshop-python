def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod() #automatically validate the embedded tests

import unittest
class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertAlmostEqual(average([20, 30, 70]), 40.0)
        self.assertAlmostEqual(round(average([1, 5, 7]),1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() #calling from the command line invokes all tests
