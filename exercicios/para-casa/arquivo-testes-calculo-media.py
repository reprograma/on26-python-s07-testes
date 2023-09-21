# Mapeando e testando cenários para o código de cálculo da média

import unittest     # importando o framework

from arquivo_calculo_media import calcular_media     # importando o arquivo fonte

class TesteMedia(unittest.TestCase):     # criando a classe de testes

# definindo métodos de testes

# 1. Lista notas zeradas
    def teste_notas_zero(self):
        resultado = calcular_media([0,0,0])
        self.assertEqual(resultado, 0)

# 2. Lista notas negativas
    def teste_notas_negativas(self):
        resultado = calcular_media([-8, -5, -10])
        self.assertAlmostEqual(resultado, -7.67, places=2)

# 3. Lista notas positivas
    def teste_notas_positivas(self):
        resultado = calcular_media([9, 3, 7])
        self.assertAlmostEqual(resultado, 6.33, places=2)

# 4. Lista notas positivas e negativas
    def teste_notas_positivas_negativas(self):
        resultado = calcular_media([-8, 2, -14, 5])
        self.assertEqual(resultado, -3.75)

# 5. Lista notas vazia
    def teste_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, None)

# 6. Lista notas com decimais
    def teste_notas_decimais(self):
        resultado = calcular_media([3.64, 8.31, 9.04])
        self.assertAlmostEqual(resultado, 7.0, places=2)

# 7. Lista notas inválidas (não consegui fazer o tratamento do erro na função de teste)
    def teste_notas_inválidas(self):
        if calcular_media(["xxx", 5, "rr"]):
            self.assertRaises(ValueError)


if __name__ == '__main__':     # chamando e executando os testes
    unittest.main()