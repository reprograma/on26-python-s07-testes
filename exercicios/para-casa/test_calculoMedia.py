import unittest 
from calculo_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista(self):
        resultado = calcular_media([6, 5, 9, 8])
        self.assertEqual(resultado, 7)

if __name__ == '__main__':
    unittest.main()