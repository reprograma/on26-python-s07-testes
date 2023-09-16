def divisao(a, b):
    return a / b

import unittest

class Testdivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertAlmostEqual(divisao(80,2),40)

    def test_divisao_negativos(self):
        self.assertAlmostEqual(divisao(-4,-4),1)
    
    def test_divisao_zeros(self):
        self.assertAlmostEqual(divisao(0,8),0)

    def  test_divisao_de_sinais_diferentes(self):
        self.assertAlmostEqual(divisao(-22,2), -11)   


if __name__ == '__main__':
    unittest.main()