import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        number1 = -42
        number2 = 42
        self.assertEqual(abs(number1), number2, 'Should be absolute value of a number')
    def test_abs2(self):
        number3 = -30
        number4 = -30
        self.assertEqual(abs(number3), number4, 'Should be absolute value of a number')

if __name__ == '__main__':
    unittest.main()