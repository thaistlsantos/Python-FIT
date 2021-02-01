import random


soma = 0

fileira = 1

while fileira <=5:
    #comprimentar todos os alunos da fileira
    print('contando a fileira', fileira)

    soma_parcial = 0
    cadeira = 1

    while cadeira <= 3:
        tem_aluno = random.randint(0,1)
        print('verificando cadeira {}: {}'.format(cadeira, tem_aluno))
        soma_parcial += tem_aluno
        cadeira += 1

    
    print('A fileira {} tem {} alunos.'.format(fileira, soma_parcial))
    soma += soma_parcial
    fileira += 1

print('Total de alunos:', soma)
print('fim')
