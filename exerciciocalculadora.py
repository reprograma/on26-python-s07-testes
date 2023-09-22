def soma(a,b):
    return a + b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertAlmostEqual(soma(2,2),4)

    def test_soma_negativos(self):
        self.assertAlmostEqual(soma(-2,-2),-4)

    def test_soma_zeros(self):
        self.assertAlmostEqual(soma(0,2),2)

    def test_soma_positivos_negativos(self):
        self.assertAlmostEqual(soma(-1,1),0)

if __name__=='__main__':
    unittest.main()

def sub(a,b):
    return a - b

class TestSubtra(unittest.TestCase):
    def test_subtra_positivos(self):
        self.assertEqual(sub(2,2),0)


    def test_subtra_negativos(self):
        self.assertEqual(sub(-2,-2),0)

    def test_subra_positivos_negativos(self):
        self.assertEqual(sub(4,-3),7)

if __name__=='__main__':
    #unittest.main()

    def div(a,b):
        return a / b 

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(div(8,8),2)

    def test_divisao_negativos(self):
        self.assertEqual(div(-2,-1),1)

    def test_divisao_positivos_negativos(self):
        self.assertEqual(div(8,-8),-2)

if __name__=='__main__':
    unittest.main()

def mult(a,b):
    return a * b 

class Testmultiplica(unittest.TestCase):
    def test_multiplica_positivos(self):
        self.assertEqual(mult(5,5),25)

    def test_multiplica_negativos(self):
        self.assertEqual(mult(-8,-4),32)

    def test_multiplica_positivos_negativos(self):
        self.assertEqual(mult(8,-8),-64)

if __name__=='__main__':
    unittest.main()