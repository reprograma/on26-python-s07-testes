Cenário de Teste - Para cálculo de média 

* Entendendo o código fonte - media_aluno *

No código fonte a função calcular_media vai aceitar uma lista de notas como argumento e calcular a média das notas do aluno. Se a lista estiver vazia, a função retorna 0 para evitar uma divisão por zero.
No calcular_media_aluno(), será criado uma lista de notas do aluno como exemplo. e será chamada a função calcular_media com essa lista.
Por fim será  exibida a média calculada com duas casas decimais usando uma string.


* Cenários de Teste *

Foi importada  a função calcular_media do arquivo media_aluno.py.

Em seguida, defini a classe de teste TestCalculoMedia que herda de unittest.TestCase.
Dentro dessa classe, consta cinco cenários  de teste diferentes:

    1. Lista vazia (test_media_lista_vazia): Testa se a função calcula a média corretamente quando a lista de notas está vazia. E o resultado esperado é zero;

    2. Notas com números positivs (test_media_notas_positivas): Testa a média de notas positivas. E retorna a média, um número positivo;

    3. Notas com números negativos (test_media_notas_negativas): Testa a média de notas negativas. E retorna a média, um número negativo;

    4. Notas com números mistos (test_media_mistura_notas): Testa a média quando a lista de notas inclui valores positivos e negativos. Verifica se a função lida corretamente com esses dados e retorna a média, levando em consideração o cálculo de números positivos e negativos;

     5. Notas com erro de digitação (test_media_erros_de_digitacao): com notas que contêm um valor não numérico , por exemplo se o usuário digitar uma lera ao invés de um número, ('A'). Esperamos que isso resulte em uma exceção TypeError.




