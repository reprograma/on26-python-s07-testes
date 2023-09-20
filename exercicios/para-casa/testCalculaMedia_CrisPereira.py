# Exercício para casa semana 07 - prof Jéssica Lima
# Estudante Cris Pereira
# Testando um código que calcula média simples de um vetor
# Testar 3 valores positivos. Resultado esperado: positivo, depois de soma dos termos, divisão pelo tamanho do conjunto.
# Testar 3 valores positivos. Resultado esperado: positivo, depois de soma dos termos, divisão pelo tamanho do conjunto. 

# positivos, negativos, positivo/negativo, zerados, vazios, letras, média simples versus ponderada
import unittest
from calculaMedia_CrisPereira import calcular_media

class TestCalculaMedia (unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado,0)

if __name__ == '__main__':
    unittest.main()