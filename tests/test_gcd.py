import unittest
from calc.app import gcd as tested_gcd

class TestSum(unittest.TestCase):

    def test_smoke1(self):
        self.assertEqual(tested_gcd(1071, 462), 21)

    def test_smoke2(self):
        self.assertEqual(tested_gcd(462, 1071), 21)

    def test_same(self):
        self.assertEqual(tested_gcd(23, 23), 23)


if __name__ == '__main__':
    unittest.main()