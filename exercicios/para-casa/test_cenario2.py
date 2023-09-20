import unittest
from Cenario2 import calculo_juros
#Cenário 2 - Cálculo de juros - Possibilidades de teste
class TestCalcularJuros(unittest.TestCase):
# 1. Lista de números positivos
  def test_juros_lista_positivos(self):
    resultado = calculo_juros(100,0.2) 
    self.assertEqual(resultado, 20.0) 

# 2. Lista onde todos os números são vazios
class TestCalcularMedia(unittest.TestCase):
  def test_media_lista_vazia(self):
    resultado = calculo_juros(0,0) 
    self.assertEqual(resultado, 0) 

# 3. Lista onde todos os números são negativos
  def test_media_lista_negativos(self):
    resultado = calculo_juros(-2,2.0) 
    self.assertEqual(resultado, -4.0) 

# 4. Lista que contém números decimais
  def test_media_lista_decimais(self):
    resultado = calculo_juros(1.5,2.3) 
    self.assertEqual(resultado, 3) 

if __name__ == '__main__':
  unittest.main()

