import unittest

from test import add, multi, divide

class TestCal(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 1), 1)

        self.assertNotEqual(add(2, 3), 6)

    def test_multi(self):
        self.assertEqual(multi(2, 3), 6)


    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)

        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()



