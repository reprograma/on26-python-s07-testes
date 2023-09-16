def divisao(a, b):
    return a / b

import unittest 

class TestDivisao(unittest.TestCase):
    def test_divisão_positivos(self):
        self.assertEqual(divisao(10, 2), 5)

    def test_div_negativos(self):
        self.assertEqual(divisao(-14, -7), 2)

    def test_div_misto(self):
        self.assertEqual(divisao(-12, 3), -4)

    def test_div_zero(self):
        self.assertEqual(divisao(0, 2), 0)

if __name__ == '__main__':
    unittest.main()