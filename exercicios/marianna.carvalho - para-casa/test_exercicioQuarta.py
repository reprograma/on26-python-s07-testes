# Cenários de Teste (Quais testes podemos fazer de uma média?)

# - Se está acima de um valor específico
# Resultado:

# - Se está abaixo de um valor específico
# Resultado:

# - Se apenas um valor foi apresentado
# Resultado:

# - Se apenas dois valores foram apresentados 
# Resultado:

import unittest
from exercicio_quarta import calcular_media

# - Se está zerada
# Resultado:

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

# - De apenas números negativos
# Resultado:

    def test_media_numeros_negativos(self):
        resultado = calcular_media([-2, -3, -4])
        self.assertEqual(resultado, -3)


if __name__ == '__main__':
    unittest.main()