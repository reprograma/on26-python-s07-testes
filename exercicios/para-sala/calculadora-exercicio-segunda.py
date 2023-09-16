
## atividade casa fazer as operçãoe sfaltantes (bub, mult, div)
def  soma(a,b):
    return a + b


def  sub(a,b):
    return a - b

def mult(a,b):
    return a * b


def div(a,b):
    if b == 0:
        # Lidar com o caso de divisão por zero
        return "indefinido"
    return a / b


import unittest


class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual (soma(2,3), 5)
    
    def test_soma_negativos(self):
        self.assertEqual (soma(-3,-3), -6)
        
    def test_soma_zeros(self):
        self.assertEqual (soma(0,0), 0)    
    
    def test_soma_positivos_negativos(self):
        self.assertEqual (soma(-4,2),-2 )   ## assertEquel é um metodo da classe 
        
        

        
class TestSub(unittest.TestCase):
        def test_sub_positivos(self):
            self.assertEqual (sub(3,2), 1)
        
        def test_sub_negativos(self):
            self.assertEqual (sub(-3,-3), 0)
            
        def test_sub_zeros(self):
            self.assertEqual (sub(0,0), 0)    
        
        def test_sub_positivos_negativos(self):
            self.assertEqual (sub(-4,2),-6 )   ## assertEquel é um metodo da classe     
            
            
class TestMult(unittest.TestCase):
        def test_mult_positivos(self):
            self.assertEqual (mult(3,2), 6)
        
        def test_mult_negativos(self):
            self.assertEqual (mult(-3,-3), 9)
            
        def test_mult_zeros(self):
            self.assertEqual (mult(0,0), 0)    
        
        def test_mult_positivos_negativos(self):
            self.assertEqual (mult(-4,2),-8 )   ## assertEquel é um metodo da classe               
            
            

class TestDiv(unittest.TestCase):
        def test_div_positivos(self):
            self.assertEqual (div(4,2), 2)
        
        def test_div_negativos(self):
            self.assertEqual (div(-6,-3), 2)
            
        def test_div_zeros(self):
            self.assertEqual (div(0,0),"indefinido")    
        
        def test_div_positivos_negativos(self):
            self.assertEqual (div(-8,2),-4 )      
            
   
    

if __name__=='__main__':
     unittest.main()
    
