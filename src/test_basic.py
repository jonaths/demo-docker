import unittest

from tools import sumar


class TestBasic(unittest.TestCase):

    def setUp(self):
        pass

    def test_one(self):
        self.assertTrue(True)

    def test_sumar(self):
        a = 2
        b = 5
        result = sumar(a, b)
        self.assertTrue(result, 5)


if __name__ == '__main__':
    unittest.main()
