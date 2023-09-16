def subtracao(a, b):
    return a - b

import unittest

class Testsubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertAlmostEqual(subtracao(10,7),3)

    def test_subtracao_negativos(self):
        self.assertAlmostEqual(subtracao(-4,-4),0)
    
    def test_subtracao_zeros(self):
        self.assertAlmostEqual(subtracao(0,9),-9)

    def  test_subtracao_de_sinais_diferentes(self):
        self.assertAlmostEqual(subtracao(5,-1), 6)   


if __name__ == '__main__':
    unittest.main()