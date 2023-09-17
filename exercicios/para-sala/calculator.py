import unittest

def sum(a,b):
    return a+b

class TestingSum(unittest.TestCase):
    def test_sum_positive(self):
        self.assertAlmostEqual(sum(4,4),8)

    def test_sum_negative(self):
        self.assertAlmostEqual(sum(-4,-4),-8)
    
    def test_sum_zero(self):
        self.assertAlmostEqual(sum(0,4),4)

    def test_sum_negative_positive(self):
        self.assertAlmostEqual(sum(5,-6), -1)
        
    


if __name__=="__main__":
    unittest.main()