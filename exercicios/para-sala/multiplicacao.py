def multiplicacao(a,b):
    return a * b

import unittest

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(5, 3), 15)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-3, -3), 9)

    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicacao(0, 1), 0)

    def test_multiplicacao_negativos_positivos(self):
        self.assertEqual(multiplicacao(-1, 2), -2)

if __name__ == '__main__':
    unittest.main()