# O que pode ser calculado de um conjunto: média simples, média ponderada, moda, mediana, variância, desvio padrão, normalizar médias da sala
# com números positivos, negativos, positivo/negativo, zerados, vazios, letras

import statistics

# class CalculaTendencia:
#     def __init__(self, notas):
#         self.notas = notas

#     def calcular_media (self):
#         return sum(self.notas)/len(self.notas)
    
#     def identificar_moda (self):
#        return statistics.mode(self.notas)
       
#     def identificar_mediana(self):
#         return statistics.median(self.notas)
    
#     def calcular_variancia (self):
#         statistics.pvariance(self.notas)

#     def calcular_desviopadrao(self):
#         statistics.pstdev(self.notas)

# class CalculaMediaPonderada(CalculaTendencia):
#     def __init__ (self, notas, pesos):
#         super().__init__(notas)
#         self.pesos = pesos
        
#     def calcular_media (self): 
#         return sum(self.notas)/sum(self.pesos)

def calcular_media (notas):
    return sum(notas)/len(notas)
    
def identificar_moda (notas):
    return statistics.mode(notas)
       
def identificar_mediana(notas):
    return statistics.median(notas)
    
def calcular_variancia (notas):
    statistics.pvariance(notas)

def calcular_desviopadrao(notas):
    statistics.pstdev(notas)

def calcular_media_ponderada (notas,pesos): 
    return sum(notas)/sum(pesos)

print("**Programa calculando média escolar**")
print("Este programa calcula a média dos alunos individualmente e oferece dados sobre a turma. É possível escolher média simples ou ponderada, também verificar a média da turma, a moda, a mediana, a variância, o desvio padrão e a normalização das médias.")

print("\nEscolha a opção desejada abaixo:")
print("1 - Adicionar turma")
print("2 - Adicionar notas e calcular média de um alune")
print("3 - Exibir informações de um alune")
print("4 - Atualizar informações de um alune")
print("5 - Exibir informações da turma")
print("0 - Sair")

def menu():
    while True:
        opcao = input("\nMENU: Digite o número da opção desejada: ")

        match opcao:
            case "1":
                return nova_turma()
            case "2":
                return novo_aluno()
            case "3":
                return print("Informações do aluno")
            case "4":
                return print("atualizar")
            case "5":
                return print("exibir")
            case "0":
                break
            case _:
                print("Opção inválida, por favor escolha uma opção do menu.")


turmas_escola = []
def nova_turma ():
    nome_turma = input("Digite o nome da turma: ")
    qtde_atividades = int(input("Digite a quantidade de atividades que a turma fará no período do curso: "))
    pergunta_pesos = input("As atividades terão pesos? Digite S ou N: ")

    id_turma = 1
    if len(turmas_escola) > 0:
        qtde_turmas = len(turmas_escola)
        id_turma = turmas_escola[qtde_turmas-1].get("id_turma")+1

    nova_turma = {
        "id_turma": id_turma,
        "nome": nome_turma,
        "qtde_atividades": qtde_atividades,
        "resposta_pesos": pergunta_pesos
    }

    if pergunta_pesos == "S":
        for cada_peso in range(qtde_atividades):
            nova_turma[f"peso{cada_peso+1}"] = float(input(f"Digite o peso da atividade {cada_peso+1}: "))

    turmas_escola.append(nova_turma)
    menu()

alunos = [] 
def novo_aluno():
    id_turma = int(input("Digite o id da turma que o aluno será inserido: "))
    verificador_peso = ""
    index_turma = 0
    num_matricula = 1
    if len(alunos) > 0:
            qtde_alunos = len(alunos)
            num_matricula = alunos[qtde_alunos-1].get("num_matricula")+1

    nome_alune = input("Digite o nome do alune: ")

    for index in range(len(turmas_escola)):
        if turmas_escola[index].get("id_turma") == id_turma:
            index_turma = index
            qtde_atividades = turmas_escola[index]["qtde_atividades"]
            verificador_peso = turmas_escola[index]["resposta_pesos"]
            break
  

    aluno = {
        "id_turma": id_turma,
        "nome": nome_alune,
        "num_matricula": num_matricula, 
    }

    notas = []
    for atividades in range(qtde_atividades):
        nota = float(input(f"Digite a nota da atividade {atividades+1}: "))
        aluno[f"nota{atividades+1}"] = nota
        notas.append(nota)

    alunos.append(aluno)

    if verificador_peso != "S":
        aluno["media"] = calcular_media(notas)
    else:
        pesos = []
        for cada_peso in range(qtde_atividades):
            pesos.append(turmas_escola[index_turma].get(f"peso{cada_peso+1}"))
        aluno["media"] = calcular_media_ponderada(notas,pesos)

    print(f" A média do alune é: {aluno['media']}")    

menu()