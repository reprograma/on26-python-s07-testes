# Exercício 1: 'Faça um arquivo contendo ao menos 4 cenários de 
# testes mapeados por você, com descrição e resultado esperado'

# Cenário de testes para cáculos de média aritmética:

# Média aritmética = Soma dos Valores dos Itens dividido pela Quantidade Total de Itens
# Exemplo: 10 e 30
# Valor 10 somado ao valor 30 = Soma dos Valores do Itens = 40
# Quantidade Total de Itens = 2 (item 10 e item 30)
# Média = 40 dividido por 2
# Média = 20

# Média de itens iguais:
# 5, 5 e 5
# 5+5+5 / 3 = 5

# Média com poucos itens:
# 2 e 8
# 2+8 / 2 = 5

# Média com muitos itens:
# 2, 10, 38, 9872, 75, 833, 662, 47, 17
# 2+10+38+9872+75+833+662+47+17 / 9 = 1284

# Média com apenas um item:
# 10
# 10 / 1 = 10

# Média com números negativos:
# -538, 80 e -382
# (-538)+(80)+(-382) / 3 = -280

# Média com frações:
# (13,69), (82,08) e (15,00)
# (13,69)+(82,08)+(15,00) / 3 = 36,92333...

# Média sem nenhum item:
# Nulo
# Mensagem de Erro: "É necessário envio de valores numéricos para calcular a média"

# Média de itens inválidos:
# 15, 50, Pedra
# Mensagem de Erro: "Não é permitido o envio de valores não numéricos para calcular a média"

#########################################################################################

# Exercício 2: 'Faça um Arquivo Python calculando a média de uma lista de números'

def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)