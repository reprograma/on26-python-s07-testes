def soma(a, b):
    return a / b

import unittest

class TestSoma(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertAlmostEqual(soma(80,2),40)

    def test_divisao_negativos(self):
        self.assertAlmostEqual(soma(-4,-4),1)
    
    def test_divisao_zeros(self):
        self.assertAlmostEqual(soma(0,8),0)

    def  test_divisao_de_sinais_diferentes(self):
        self.assertAlmostEqual(soma(-22,2), -11)   


if __name__ == '__main__':
    unittest.main()