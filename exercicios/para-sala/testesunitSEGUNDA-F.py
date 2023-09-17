#SOMA
def soma(a,b):
    return a+b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertAlmostEqual(soma(4,4),8)

    def test_soma_negativos(self):
        self.assertAlmostEqual(soma(-4,-4),-8)
    
    def test_soma_zeros(self):
        self.assertAlmostEqual(soma(0,4),4)

    def test_soma_positivos_negativos(self):
        self.assertAlmostEqual(soma(-3,3),0)

if __name__=='__main__':
    unittest.main()

#SUBTRAÇÃO

def sub(a,b):
    return a-b

class TestSubtra(unittest.TestCase):
    def test_subtra_positivos(self):
        self.assertEqual(sub(4,4),0)


    def test_subtra_negativos(self):
        self.assertEqual(sub(-4,-4),0)

    def test_subra_positivos_negativos(self):
        self.assertEqual(sub(5,-4),9)

if __name__=='__main__':
    #unittest.main()

#DIVISÃO

    def div(a,b):
        return a/b 

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(div(4,4),1)

    def test_divisao_negativos(self):
        self.assertEqual(div(-4,-2),2)

    def test_divisao_positivos_negativos(self):
        self.assertEqual(div(4,-4),-1)

if __name__=='__main__':
    unittest.main()

#MULTIPLICAÇÃO

def mult(a,b):
    return a*b 

class Testmultiplica(unittest.TestCase):
    def test_multiplica_positivos(self):
        self.assertEqual(mult(4,4),16)

    def test_multiplica_negativos(self):
        self.assertEqual(mult(-4,-2),8)

    def test_multiplica_positivos_negativos(self):
        self.assertEqual(mult(4,-4),-16)

if __name__=='__main__':
    unittest.main()