def subtracao(a,b):
    return a - b

import unittest

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(5, 3), 2)

    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-3, -3), 0)

    def test_subtracao_zero(self):
        self.assertEqual(subtracao(0, 0), 0)

    def test_subtracao_negativos_positivos(self):
        self.assertEqual(subtracao(-1, 2), -3)

if __name__ == '__main__':
    unittest.main()