from time import sleep

entrada = input('Digite os números separados por espaço:')

numeros = entrada.split()

for x in numeros: 
    print(x, end='...')



for x in range(5, -1, -1): 
    print('resultado é {}, '.format(x), end='')
    sleep(1)
    input('enter para continuar...')

