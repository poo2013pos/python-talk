import unittest

def factorial(n):
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

class FactorialTests(unittest.TestCase):
    def test_ints(self):
        self.assertEqual(
            [factorial(n) for n in range(6)], [1, 1, 2, 6, 24, 120])

    def test_long(self):
        self.assertEqual(
            factorial(30), 265252859812191058636308480000000L)

    def test_negative_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
