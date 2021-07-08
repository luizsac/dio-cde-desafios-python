# Enunciados

### Folha de Pagamento:

Precisamos saber quanto uma determinada empresa deve pagar para seus colaboradores, porém temos apenas a quantidade de horas trabalhadas e o valor hora. Escreva um programa que leia o número de um colaborador, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse colaborador. Em seguida, apresente o número e o salário do colaborador, com duas casas decimais.

<br>

Entrada

Você receverá 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada.

<br>

Saída

Exiba o número e o salário do colaborador, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

| Exemplo de Entrada | Exemplo de Saída |
| ---- | ---- |
| 25 <br> 100 <br> 5.50 | NUMBER = 25 <br> SALARY = U$ 550.00 |
| 1 <br> 200 <br> 20.50 | NUMBER = 1 <br> SALARY = U$ 4100.00 |
| 6 <br> 145 <br> 15.55 | NUMBER = 6 <br> SALARY = U$ 2254.75 |

<br>

### Média 3:

Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

<br>

Entrada

A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

<br>

Saída

Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

| Exemplo de Entrada | Exemplo de Saída |
| ---- | ---- |
| 2.0 4.0 7.5 8.0 <br> 6.4 | Media: 5.4 <br> Aluno em exame. <br> Nota do exame: 6.4 <br> Aluno aprovado. <br> Media final: 5.9 |
| 2.0 6.5 4.0 9.0 | Media: 4.8 <br> Aluno reprovado. |
| 9.0 4.0 8.5 9.0 | Media: 7.3 <br> Aluno aprovado. |

<br>

### Notas da Prova:

Norminia é uma professora e pesquisadora renomada de uma famosa Universidade do Brasil, com inúmeras prêmiações e reconhecimento internacional pelo seu trabalho. Recentemente, Norminia foi convidada para ministrar aulas em uma Universidade da Alemanhã. Mesmo falando muito bem a Língua alemã, Norminia ficou um pouco apreensiva com a responsabilidade, mas resolveu aceitar a proposta e encará-la como um bom desafio.

Os estudantes adoraram a metodologia de ensino de Norminia e tudo estava indo super bem, até o momento da aplicação da sua primeira prova. Acostumada a dar notas de 0 (zero) a 100 (cem), ela fez o mesmo na primeira prova da sua turma da Alemanhã. No entanto, os estudante acharam estranho, uma vez que na Alemanhã o sistema de notas é diferente: as notas devem ser dadas como conceitos de A a E. O conceito A é o mais alto, enquanto o conceito E é o mais baixo.

Conversando com outros docentes, ela recebeu a sugestão de utilizar a seguinte tabela, relacionando as notas numéricas com as notas de conceitos:
| Nota | Conceito |
|:-:|:-:|
| 0 | E |
| 1 a 35 | D |
| 36 a 60 | C |
| 61 a 85 | B |
| 86 a 100 | A |

O problema é que Norminia já deu as notas no sistema numérico, e terá que converter as notas para o sistema de letras. No entanto, Norminia precisa preparar as próximas atividades educacionais para os seus alunos, e não tem tempo suficiente para fazer a conversão das notas manualmente.

Você terá o seguinte desafio: escrever um programa que recebe uma nota no sistema numérico e determina o conceito correspondente.

<br>

Entrada

A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A entrada contém uma única linha com um número inteiro N (0 ≤ N ≤ 100), representando uma nota de prova no sistema numérico.

<br>

Saída

Seu programa deve imprimir, na saída padrão, uma letra (A, B, C, D, ou E em maiúsculas) representando o conceito correspondente à nota dada na entrada.

| Exemplo de Entrada | Exemplo de Saída |
| ---- | ---- |
| 12 | D |
| 87 | A |
| 0 | E |

<br>

### Preenchimento de Vetor I:

Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

<br>

Entrada

A entrada contém um valor inteiro (V<=50).

<br>

Saída

Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.

| Exemplo de Entrada | Exemplo de Saída |
| ---- | ---- |
| 1 | N[0] = 1 <br> N[1] = 2 <br> N[2] = 4 |

<br>

### Programa para Validação de Notas:

O calendário escolar está passando bem rápido, devido a isso, as professoras de uma escola estão com dificuldade para calcular as notas dos alunos. Visando em resolver a situação, a diretora da escola contratou você para desenvolver um programa que leia as notas da primeira e da segunda avaliação de um aluno. Calcule e imprima a média semestral.

O programa só aceitará notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando as professoras que informe um código (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

<br>

Entrada

O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve ser lido um valor inteiro X . O programa deve parar quando o valor lido para este X for igual a 2.

<br>

Saída

Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas, deve ser impressa a mensagem “media = ” seguido do valor do cálculo.

Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada novamente se o valor da entrada padrão para X for menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.

| Exemplo de Entrada | Exemplo de Saída |
| ---- | ---- |
| -3.5 <br> 3.5 <br> 11.0 <br> 10.0 <br> 4 <br> 1 <br> 8.0 <br> 9.0 <br> 2 | nota invalida <br> nota invalida <br> media = 6.75 <br> novo calculo (1-sim 2-nao) <br> novo calculo (1-sim 2-nao) <br> media = 8.50 <br> novo calculo (1-sim 2-nao) |

<br>

### Triângulo:

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

<br>

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:

Area = XX.X

<br>

Entrada

A entrada contém três valores reais.

<br>

Saída

O resultado deve ser apresentado com uma casa decimal.

<br>

| Exemplo de Entrada | Exemplo de Saída |
| ---- | ---- |
| 6.0 4.0 2.0 | Area = 10.0 |
| 6.0 4.0 2.1 | Perimetro = 12.1 |
