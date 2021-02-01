valido = False

while not valido:
    n = int(input('Digite um número par no intervalo de [1, 50]: '))

    no_intervalo = 1 <= n and n <=50
    eh_par = n % 2 == 0

    if no_intervalo and eh_par:
        valido = True
    else:
        print('Número fora do intervalo, tente novamente')

print('Número aceito')
