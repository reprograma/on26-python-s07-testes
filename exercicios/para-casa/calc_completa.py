def soma(a,b):
    return a+b #essa funcao é criada depois do teste dar errado

import unittest

class TestSoma(unittest.TestCase):
    def teste_soma_positivos(self):
        self.assertEqual(soma(2,3),5) #assertEqual é como se fosse um comando, dizendo que é igual 
                       

    def test_soma_negatvios(self):
        self.assertEqual(soma(-3,-3),-6)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0),0)


    def test_posneg(self):
        self.assertEqual(soma(-7, 5), -2)
  
    
if __name__ == '__main__': #== pq nao ta recebendo, esta comparando
    unittest.main()


    
def subtr(a,b):
    return a-b

class TesteSubtr(unittest.TestCase):
    def teste_subtr_positivos(self):
        self.assertEqual(subtr(8,3),5)
        
        
    def test_subtr_negativos(self):
        self.assertEqual(subtr(-10, 5), 5)
        self.assertEqual(subtr(5, -7), -2) #DUVIDAA
        
    
if __name__ == "__main__":
    unittest.main()


    
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
    
class TesteDiv(unittest.TestCase):
    def teste_div_positivos(self):
        self.assertEqual(div(20, 4), 5)    
        
        
    def teste_div_negativos(self):
        self.assertEqual(div(-10, -5), 2)
        self.assertEqual(div(-20, 10), -2)
        
    def teste_div_zeros(self):        
        self.assertEqual(div(0, 10), 0)
        with self.assertRaises(ZeroDivisionError):
            (div(10, 0), 0)
    
        
if __name__ == "__main__":
    unittest.main()
    
    

def multipl(a, b):
    return a*b     
    
    class TesteMultipl(unittest.TestCase):
        def teste_multipl_positivos(self):
            self.assertEqual(multipl(8, 5), 40)
    
    def teste_multipl_negativos(self):
        self.assertEqual(multipl(-5, 6), -30)
    def teste_multipl_negativos(self):
        self.assertEqual(multipl(-4, -3), 12)
    
    
if __name__ == '__main__':
    unittest.main()
    