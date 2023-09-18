def divisao(a,b):
    return a / b

import unittest

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(divisao(15, 3), 5)

    def test_divisao_negativos(self):
        self.assertEqual(divisao(-3, -3), 1)

    def test_divisao_zero(self):
        self.assertEqual(divisao(0, 0), 0)

    def test_divisao_negativos_positivos(self):
        self.assertEqual(divisao(-10, 2), -5)

if __name__ == '__main__':
    unittest.main()