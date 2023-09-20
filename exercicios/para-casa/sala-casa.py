
# Tentar quebrar o código de média aritmética 
## Calculando a média de uma lista 

def calcular_media(numeros):
    if not numeros:
        return 0
    
    return sum(numeros) / len(numeros)
import unittest
from atividade_testes_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)
if name_ == "__main__":
    unittest.main()
      






