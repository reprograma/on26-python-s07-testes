import unittest
from calcula_media import calculaMedia

# Cria uma classe de teste chamada testCalculaMedia que herda da classe TestCase
class testCalculaMedia(unittest.TestCase):

    # Teste 1: Verifica se a função calculaMedia retorna 0 para uma lista vazia.
    def teste_lista_vazia(self):
        resultado = calculaMedia([])
        self.assertEqual(resultado, 0)  # Compara o resultado com o valor esperado (0).

    # Teste 2: Verifica se a função calculaMedia retorna o número 5 quando a lista contém apenas o número 5.
    def teste_um_numero(self):
        resultado = calculaMedia([5])
        self.assertEqual(resultado, 5)  # Compara o resultado com o valor esperado (5).

    # Teste 3: Verifica se a função calculaMedia retorna a média (3) de uma lista de números positivos de 1 a 5.
    def teste_numeros_positivos(self):
        resultado = calculaMedia([1, 2, 3, 4, 5])
        self.assertEqual(resultado, 3)  # Compara o resultado com o valor esperado (3).

    # Teste 4: Verifica se a função calculaMedia retorna a média (-3) de uma lista de números negativos de -1 a -5.
    def teste_numeros_negativos(self):
        resultado = calculaMedia([-1, -2, -3, -4, -5])
        self.assertEqual(resultado, -3)  # Compara o resultado com o valor esperado (-3).

    # Teste 5: Verifica se a função calculaMedia retorna a média (-0.6) de uma lista de números mistos.
    def teste_numeros_mistos(self):
        resultado = calculaMedia([-1, 2, -3, 4, -5])
        self.assertEqual(resultado, -0.6)  # Compara o resultado com o valor esperado (-0.6).

# Inicializa a execução dos testes se este arquivo for executado diretamente.
if __name__ == '__main__':
    unittest.main()
