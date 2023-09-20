"""Questão 1-
    Testes hipotéticos para calcular Média:
    1- media da lista vazia - se a lista estivar vazia retorne 0
    2 - media divisão por zero -  se a soma da media der zero retorna uma media = 0
    3 - numeros negativos - a soma dos numero negativa a média retorna uma media megativo
    4 - numeros positivos - a soma dos numeros positivos <= 10 retorna umamedia posiviva <=10
    5 - numeros maiores que 10 - a soma dos numeros retorna uma media > 10
    6 - numeros iguais - a soma dos numeros iguais retorna uma media = e ele mesmo
    7 - numeros positivos e negativos intercalados = a soma dos numeros retorna uma media  negativo
    8 - numeros reais positivos - a somo dos numeros fracionariospositivos retorna uma media fracionaria positiva
    9 - um unico numero - o unico numero retorna uma media = a esse numero unico
    10 - valores não numeris - a soma dos valores não numericos retorna uma média nula(None)
    para realizar esse ultimo modifiquei o função proposta aqui inicialmente 
    def calcular_media(numeros):
    if not numeros:
        return None 
    return sum (numeros)/ len(numeros)
    """


# Quetão 2
import unittest
import math

from calculo_media import calcular_media


class TestCalcularmedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado,None)
        
    def test_media_divisao_por_zero(self):
        resultado = calcular_media([0, 0, 0])
        self.assertEqual (resultado, 0)


    def test_media_numero_negativo(self):
        resultado = calcular_media([-2, -3, -1])
        self.assertEqual (resultado, -2.0)

    
    def test_media_numero_positivo_menor_ou_igual_10 (self):
        resultado = calcular_media([5, 9, 6, 4])
        self.assertEqual(resultado,6.0 )
        
        
    def test_media_numero_maior_que_10(self):
        resultado = calcular_media([13, 15, 19,11,10])
    
        self.assertGreater (resultado, 10) # verifica se a media é menor uq 10
    
    
    def test_media_numeros_iguais(self):
        resultado = calcular_media([2,2,2,2,2])
    
        self.assertEqual(resultado, 2.0)
        
        
    def test_media_positivos_negativos_intercalados(self):
        resultado = calcular_media([-3, 5, -9,1,-8])
    
        self.assertLessEqual(resultado, -2.8)
        
    
    def test_media_reais_positivos(self):
        resultado = calcular_media([3.4, 5.8, 9.5,1.2,8.7])
    
        self.assertEqual(resultado, 5.72)    
    
    
    def test_media_nota_unica(self):
        resultado = calcular_media([3.4])
    
        self.assertEqual(resultado, 3.4)  
        
         
        
    def test_media_valores_nao_numericos(self):
        resultado = calcular_media(['a', 'b', 'c','d','e'])
    
        self.assertIsNone(resultado, None)      
        

if __name__ == '__main__':
    unittest.main()
        
        
        
    
    