import unittest

def multiplication(a,b):
    return a*b
        
class TestingMultiplication(unittest.TestCase):   
    def test_multiplication_positive(self):
        self.assertAlmostEqual(multiplication(4, 2), 8)    
                                   
    #def test_multiplication_negative(self):
    #    self.assertAlmostEqual(multiplication(-2, -2), -4)
    
    def test_multiplication_zero(self):
        self.assertAlmostEqual(multiplication(0, 444), 0)
        
    def test_multiplication_positive_negative(self):
        self.assertAlmostEqual(multiplication(5, -2), -10)
    
    
if __name__=="__main__":
    unittest.main()