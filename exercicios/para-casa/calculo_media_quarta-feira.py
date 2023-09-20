# Possibilidades de teste:
# 1- Verificar o cálculo da média com números positivos floats (o resultado será float)
# 2- Verificar o cálculo da média com números positivos floats e ints (o resultado será float)
# 3- Verificar a soma entre numeros positivos e a divisão por um número positivo
# 4- Verificar se o divisor é sempre positivo
# 5- Verificar a soma de termos iguais a 0 e a divisão pelo número de termos (o resultado será 0)
# 6- Verificar se o divisor realmente corresponde ao número de termos do dividendo
# 7- Verificar a obtenção de um float com no máximo 2 casas decimais no resultado ao trabalharmos com floats no dividendo
# 8- Verificar a obtenção de um float com no máximo 2 casas decimais no resultado ao trabalharmos com floats e inteiros no dividendo
# 9- Calcular a média usando floats no dividendo e arredondando para cima
# 10- Calcular a média usando floats no dividendo e arredondando para baixo
# 11- Calcular a média usando floats e inteiros no dividendo e arredondando para cima
# 12- Calcular a média usando floats e inteiros no dividendo e arredondando para baixo
# 13 - Calcular a média usando floats no dividendo e arredondando o resultado para cima ou para baixo seguindo a regra da matemática

import unittest
from media_aritmedica import calcular_media


class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)          #se a lista estiver vazia, obrigatoriamente o resultado será 0

#1- Verificar o cálculo da média com números positivos floats (o resultado será float)   
class TestCalcularMediaComFloats(unittest.TestCase):
    def test_media_com_floats(self):
        resultado = calcular_media([8.0, 8.0, 9.0])
        self.assertAlmostEqual(resultado, 8.3, places=1)

# 2- Verificar o cálculo da média com números positivos floats e ints (o resultado será float)
class TestCalcularMediaComFloatsEInts(unittest.TestCase):
    def test_media_com_floats_e_ints(self):
        resultado = calcular_media([7, 9.8, 8.5, 6])
        self.assertAlmostEqual(resultado, 7.8, places=1)

# 9- Calcular a média usando floats no dividendo e arredondando para cima
class TestCalcularMedia_Floats_ResultadoArredondadoParaCima(unittest.TestCase):
    def test_media_floats_resultado_arredondado_para_cima(self):
        resultado = calcular_media([8.0, 3.0, 12.0, 5.5])
        self.assertEqual(round(resultado + 0.5), 8)

# 12- Calcular a média usando floats e inteiros no dividendo e arredondando para baixo
class TestCalcularMedia_FloatsEInts_ResultadoArredondadoParaBaixo(unittest.TestCase):
    def test_media_floatseints_resultado_arredondado_para_baixo(self):
        resultado = calcular_media([7, 9, -5.5])
        self.assertEqual(round(resultado - 0.5), 3)

# 13 - Calcular a média usando floats no dividendo e arredondando o resultado para cima ou para baixo seguindo a regra da matemática
class TestCalcularMedia_Floats_ResultadoArredondadoParaCima_MatematicamenteCorreto(unittest.TestCase):
    def test_media_floats_arredondando_corretamente(self):
        resultado = calcular_media([4.5, 4])
        c = round(resultado - 0.5)
        if resultado - c >= 0.5:
            print(round(resultado + 0.5))
        elif resultado - c < 0.5:
            print(round(resultado - 0.5))

if __name__ == '__main__':
    unittest.main()




