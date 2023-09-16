def multiplicacao(a, b):
    return a * b

import unittest

class Testmultiplicacao(unittest.TestCase):
    def test_mult_positivos(self):
        self.assertAlmostEqual(multiplicacao(4,9),36)

    def test_mult_negativos(self):
        self.assertAlmostEqual(multiplicacao(-4,-4),16)
    
    def test_mult_zeros(self):
        self.assertAlmostEqual(multiplicacao(0,8),0)

    def  test_mult_de_sinais_diferentes(self):
        self.assertAlmostEqual(multiplicacao(-5,9), -45)   


if __name__ == '__main__':
    unittest.main()