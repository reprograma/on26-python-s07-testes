import unittest
from calculo_media import calcular_media

#Teste lista vazia:
class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()

#Teste lista com valores somente positivos:
class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_positiva(self):
        resultado = calcular_media([3,2])
        self.assertEqual(float(resultado))

if __name__ == '__main__':
    unittest.main()

#Teste lista com valores somente negativos:
class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_negativa(self):
        resultado = calcular_media([-10,-4])
        self.assertEqual(float(resultado))

if __name__ == '__main__':
    unittest.main()

#Teste lista com valores positivos e negativos:
class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_positiva_negativa(self):
        resultado = calcular_media([7,-3])
        self.assertEqual(float(resultado))

if __name__ == '__main__':
    unittest.main()

#Teste lista com valores fracionados:
class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_fracionada(self):
        resultado = calcular_media([(3/4), (9/2)])
        self.assertEqual(float(resultado))

if __name__ == '__main__':
    unittest.main()
    
#Teste lista com menos de 3 valores:
class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_menos_valores(self):
        resultado = calcular_media([2,7])
        self.assertEqual(resultado, "Mínimo 3 valores")

if __name__ == '__main__':
    unittest.main()