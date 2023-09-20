import unittest
from Cenario1 import calculo_media
#Cenário 1 - Calcular média de valores de uma lista - Possibilidades de teste: 
# 1. Lista de números vazia
class TestCalcularMedia(unittest.TestCase):
  def test_media_lista_vazia(self):
    resultado = calculo_media([]) 
    self.assertEqual(resultado, 0) 

# 2. Lista onde todos os números são negativos
  def test_media_lista_negativos(self):
    resultado = calculo_media([-2,-2,-2,-2]) 
    self.assertEqual(resultado, -2) 

# 3. Lista que contém números decimais
  def test_media_lista_decimais(self):
    resultado = calculo_media([1.5,2.3,5.9,7.2]) 
    self.assertEqual(resultado, 4.225) 

# 4. Lista com números positivos e negativos
  def test_media_lista_mistos(self):
    resultado = calculo_media([-2,4,-5,9]) 
    self.assertEqual(resultado, 1.5) 

if __name__ == '__main__':
  unittest.main()

