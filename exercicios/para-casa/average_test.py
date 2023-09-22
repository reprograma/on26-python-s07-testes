'''
1. Faça um arquivo contendo todos os cenários de teste mapeados por você, com descrição e resultado esperado (entrega em formato PDF)
2. Faça um Arquivo python calculando a média de uma lista de números
3. Faça um arquivo de teste, que contenha todos os testes mapeados por você (passo 1), para testar o arquivo python que você calculou as médias

Testa se lista vazia
Testa todos os números são iguais
Testa todos os números iguais a zero
Testa números negativos
Testa números negativos e positivos
Testa números float
'''

import unittest
from average import calcular_media

class TestCalcularMedia(unittest.TestCase):
#Testa se lista vazia
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, None)

#Testa todos os números são iguais
    def test_media_lista_igual(self):
        self.assertEqual(calcular_media([5, 5, 5]), 5)

#Testa todos os números iguais a zero
    def test_media_lista_zeros(self):
        self.assertEqual(calcular_media([0, 0, 0]), 0)

#Testa números negativos
    def test_media_lista_negativos(self):
        self.assertEqual(calcular_media([-5, -4, -3]), -4)

#Testa números negativos e positivos
    def test_media_lista_neg_pos(self):
        self.assertEqual(calcular_media([-5, 0, 5]), 0)

#Testa números float
    def test_media_lista_float(self):
        self.assertEqual(calcular_media([5.5, 6.5, 7.5]), 6.5)

#Testa erro de tipo de dado
    def test_media_tipo(self):
        with self.assertRaises(TypeError):
            calcular_media("a", "b")

if __name__ == "__main__":
    unittest.main()