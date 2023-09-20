# Exercício 3: 'Faça um arquivo de teste, que contenha todos os testes mapeados por você (passo 1), 
# para testar o arquivo python que você calculou as médias'

import unittest
from calculo_media_kerlla import calcular_media

class TestCalcularMedia(unittest.TestCase):
    
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)
        
        
import unittest
from calculo_media_kerlla import calcular_media

class TestCalcularMedia(unittest.TestCase):
    
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)
    
    def test_media_itens_iguais(self):
        resultado = calcular_media([5, 5, 5])
        self.assertEqual(resultado, 5)
    
    def test_media_poucos_itens(self):
        resultado = calcular_media([2, 8])
        self.assertEqual(resultado, 5)
    
    def test_media_muitos_itens(self):
        resultado = calcular_media([2, 10, 38, 9872, 75, 833, 662, 47, 17])
        self.assertEqual(resultado, 1284)
    
    def test_media_apenas_um_item(self):
        resultado = calcular_media([10])
        self.assertEqual(resultado, 10)
    
    def test_media_numeros_negativos(self):
        resultado = calcular_media([-538, 80, -382])
        self.assertEqual(resultado, -280)
    
    def test_media_com_fracoes(self):
        resultado = calcular_media([13.69, 82.08, 15.00])
        self.assertAlmostEqual(resultado, 36.923333, places=6)
    
    def test_media_sem_itens(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)
    
    def test_media_itens_invalidos(self):
        with self.assertRaises(ValueError):
            calcular_media([15, 50, "Pedra"]) # erro proposital, imaginan7do probabilidades de uso

if __name__ == '__main__':
    unittest.main()
