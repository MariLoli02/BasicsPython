import unittest
from dividir import division

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(division(10, 5), 2)
        self.assertEqual(division(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            resultado = division(1, 0)
        self.assertEqual(division(-1, -1), 1)


if __name__ == '__main__':
    unittest.main()