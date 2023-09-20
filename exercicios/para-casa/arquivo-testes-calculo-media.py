# Testando cenários mapeados para o código de cálculo da média


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

# 5. Lista notas vazia
    def teste_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, None)

# 6. Lista notas inválidas

# 7. Lista notas com decimais


if __name__ == '__main__':     # chamando e executando os testes
    unittest.main()