import unittest

def subtraction(a,b):
    return a-b
        
class TestingSubtraction(unittest.TestCase):   
    def test_subtraction_positive(self):
        self.assertAlmostEqual(subtraction(44, 22), 22)    
                                   
    def test_subtraction_negative(self):
        self.assertAlmostEqual(subtraction(-14, -7), -7)
    
    def test_subtraction_zero(self):
        self.assertAlmostEqual(subtraction(0, 4), -4)
        
    def test_subtraction_positive_negative(self):
        self.assertAlmostEqual(subtraction(-5, 4), -9)
    
    
if __name__=="__main__":
    unittest.main()