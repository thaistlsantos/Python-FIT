from time import sleep

entrada = input('Digite os números separados por espaços: ')

#split
numeros = entrada.split()

for x in numeros:
    print(x, end='...')



# #criação de arquivo:
# f = open('test.txt', 'w')
# print('ola', file= f)

