# exibir todos os númeors  de 0 a n


n = int(input('Digite o n: '))

cont = 0
while cont <= n:
    n_par = cont % 2 == 0
    print(' passo: {}, comparação: {}'
          .format(cont, n_par))
    if n_par:
        print(cont)
    cont = cont + 1
