Aula de Sábado - Prof. Jessica Lima

QA - Quality assurance
Vai assegurar a qualidade do software, produto, projeto através de testes, melhoria de processos, melhoria do software. 

Objetivo dos testes:
- garantir a entrega em acordo com a expectativa do cliente mantendo a credibilidade da empresa
- entregar com segurança protegendo informações sensíveis
- entregar com o menor número de erros possível

Benefícios dos testes:
- redução de bugs e erros (quanto mais cedo testar, mais rápido acha os bugs)
- melhoria de qualidade do software ()
- economia de tempo e recursos no longo prazo

Ciclo de vida dos testes
1. Análise: Definindo os requisitos para os testes
2. Planejamento: Definindo o plano de testes e ferramentas a serem utilizadas
3. Execução: Realização dos testes em acordo com o planejado
4. Relatório: Documentação dos testes realizados

Pirâmide de testes

Base da piramide - Teste unitário [Testa a menor parte possível do sistema - uma função, uma classe, etc.]
São usados para garantir que o código funcione de acordo com as especificações
Ex: Uma calculadora - Soma, Divisão, Subtração, Multiplicação - Cada uma cabe um teste unitário

Meio da piramide - Teste de integração [Testa o funcionamento entre as pequenas partes]
São usados para garantir que as diferentes unidades de software funcionam bem juntas
Ex: Uma calculadora - Testar todas as funções juntas 

Topo da piramide - E2E Testing (teste de ponta a ponta, teste de aceitação)
Teste de ponta a ponta, simulando o uso do cliente, testar o projeto todo.
São usados para garantir que o software esteja funcionando de acordo com as especificações do projeto e necessidades do usuário
Último teste, teste mais caro. É melhor achar lá do que no usuário. Mas é muito melhor achar no teste unitário.

Boas práticas de testes unitários
- Nova funcionalidade = novos testes
  Ao construir uma nova funcionalidade, construir um teste para essa funcionalidade. Garante que novas funções não quebrem o software.
- Crie testes simples
  Testes devem ser curtos e específicos para garantir que o comportamento esperado da função ou classe está ocorrendo corretamente
- Executar testes com frequência

Cenários de teste
Prever possíveis falhas no código para testar estas diferentes situações

*TDD - Test Driven Development
*Test coverage - quais são os tipos de testes que estão sendo realizados

----------------------------------------------------------------------------------------
Aula de Segunda-feira - Prof. Jessica Lima

Unittest - 
Framework de testes unitários 

- Como escrever testes unitários?
É preciso conhecimento sobre as funcionalidades do código, criação de casos teste para cada função e verificação de resultados esperados

- Estrutura de teste unitário
1. preparação do ambiente de teste; (análise das funcionalidades a serem testadas, análise da tecnologia de testes, planejamneto dos testes)
2. Execução do código a ser testado;
3. Verificação dos resultados obtidos em relação aos resultados esperados.

Boas práticas - 1 pasta para código ; 1 pasta para testes (importa o arquivo de código no arquivo de testes)

Testes parametrizados
Permitem executar uma mesma função de teste com diferentes conjuntos de dados para saber se a função de teste é capaz de lidar com diferentes
cenários (ex: testar com números inteiros, números positivos, números negativos, números decimais)

Code coverage - o quanto do código está sendo testado 
É uma medida da quantidade de código-fonte que está sendo testada e assim identificamos lacunas não testadas, também como identificamos qualidade do código (quanto mais testado, mais qualidade)

O que o DEV deve testar - testes unitários no código que está desenvolvendo (base da pirâmide)
O que o QA deve testar - integração do código e aceitação do código (meio e topo da pirâmide)

Boas práticas no uso do Unittest (Reforçando!):
1. Nova funcionalidade, novo teste
2. Manter testes simples e independentes
3. Testes com nomes descritivos (não tem problema ficam um nome muito grande)

Exemplos de Assert
- AssertEqual - a premissa é verificar se uma coisa é igual a outra (funciona com strings)
- AssertNotEqual - a premissa é verificar se uma coisa é necessariamente diferente da outra (não pode ser igual de jeito nenhum)
- assertTrue() - verifica se é verdadeiro, testa condições booleanas
- assertFalse() - verifica se é falso, testa condições booleanas
- AssertIsNone() - verifica se é nulo (vazio)
- AssertisNotNone () - verifica se é um valor não-vazio

