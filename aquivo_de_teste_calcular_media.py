import unittest

from exercicio_media import calcular_media
# Possíveis Cenários de Teste

#Testar média de Lista Vazia. Resultado = 0
#Testar média de Lista Preenchida = 9 , 9, 9 / 3 = 9
#Testar média de Lista de números negativos = (-7)+(-7)+(-7)/3 = -7
#Testar se a lista tiver só uma nota = resultado = a nota exemplo: [9]/ 1 = 9
# Testar se a lista tiver números 0 acompanhados de um único número acima de 0. Ex: 0,0,9 / 3 = 3
#Testar se ao colocar um número inteiro nas notas, a média é trazida ao usuário em float, caso necessário. 
#Exemplo numa divisão de notas (10 + 9 + 10/3) verificar se o resultado é trazido com casas decimais.
#Testar se calcula média de números negativos. Resultado esperado, média menor que 0.abs


class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual (resultado, 0)
    def test_media_lista(self):
        resultado = calcular_media([9,9,9])
        self.assertEqual (resultado, 9)
    def test_media_numeros_negativos(self):
        resultado = calcular_media([-7,-7,-7])
        self.assertEqual (resultado, -7)
    def test_media_de_um_numero_na_lista(self):
        resultado = calcular_media([9])
        self.assertEqual (resultado, 9 )
    def test_media_lista_com_zeros_e_algum_numero_maior_que_zero (self):
        resultado = calcular_media([0,0,9])
        self.assertEqual (resultado, 3 )
   
    def test_media_lista_float (self):
        resultado = calcular_media ([9.0,9.0,10.0])
        self.assertAlmostEqual (resultado, 9.3, places=1)
   
    def test_media_lista_int (self):
        resultado = int (calcular_media ([9,9,10]))
        self.assertEqual (resultado, 9 )
if __name__ == '__main__':
    unittest.main()