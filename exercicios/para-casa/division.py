import unittest

def division(a,b):
    return a/b
        
class TestingDivision(unittest.TestCase):   
    def test_division_positive(self):
        self.assertAlmostEqual(division(44, 2), 22)    
                                   
    def test_division_negative(self):
        self.assertAlmostEqual(division(-14, -7), 2)
    
    def test_division_zero(self):
        self.assertAlmostEqual(division(0, 4), 0)
        
    def test_division_positive_negative(self):
        self.assertAlmostEqual(division(-5, 2), -2.5)
    
    
if __name__=="__main__":
    unittest.main()