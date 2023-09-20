# Exercício para casa semana 07 - prof Jéssica Lima
# Estudante Cris Pereira
# Testando uma função que calcula média simples de um vetor
# Testar 3 valores positivos. Resultado esperado: positivo, depois de soma dos termos, divisão pelo tamanho do conjunto.
# Testar 3 valores negativos. Resultado esperado: negativo, depois de soma dos termos, divisão pelo tamanho do conjunto. 
# Testar 1 valor positivo, 2 valores negativos. Resultado esperado: negativo, depois de soma dos termos, divisão pelo tamanho do conjunto.
# Testar vetor com valores zerados. Resultado esperado: zerado. 
# Testar vetor vazio. Resultado esperado: zerado. 

from calculaMedia_CrisPereira import calcular_media
import unittest

class TestCalculaMedia (unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_lista_positivos(self):
        resultado = calcular_media([10,8,9])
        self.assertEqual(resultado, 9)

    def test_media_lista_negativos(self):
        resultado = calcular_media([-2,-9,-7])
        self.assertEqual(resultado,-6)

    def test_media_lista_ambos(self):
        resultado = calcular_media([8,-7,-10])
        self.assertEqual(resultado,-3)

    def test_media_lista_zerada(self):
        resultado = calcular_media([0,0,0])
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()