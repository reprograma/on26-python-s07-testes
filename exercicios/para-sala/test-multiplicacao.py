def multiplicacao(a, b):
    return a * b

import unittest

class TestMultiplicacao(unittest.TestCase):
    def test_mult_positivos(self):
        self.assertEqual(multiplicacao(2, 5), 10)

    def test_mult_negativos(self):
        self.assertEqual(multiplicacao(-3, -3), 9)
  
    def test_mult_zero(self):
        self.assertEqual(multiplicacao(0, 0), 0)

    def test_mult_misto(self):
        self.assertEqual(multiplicacao(3, -2), -6)

if __name__ == '__main__':
    unittest.main()

