def expressao_numerica(a, b, c, d):
    return a + (b/c)*d

import unittest

class Testexpressao_numerica(unittest.TestCase):
    def test_expre_positivos(self):
        self.assertAlmostEqual(expressao_numerica(3,4,2,3),9)

    def test_expre_negativos(self):
        self.assertAlmostEqual(expressao_numerica(-3,-4,-2,-3),-9)

    def test_expre_zero(self):
        self.assertAlmostEqual(expressao_numerica(-3,0,-2,-3),-3)    

    def test_expre_sinais_diferentes(self):
        self.assertAlmostEqual(expressao_numerica(-3,6,-2,9),-30)        


   
if __name__ == '__main__':
    unittest.main()