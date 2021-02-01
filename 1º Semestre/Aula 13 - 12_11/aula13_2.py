entrada = '1 2 3 5 6 9 7'

numeros = entrada.split()

print(numeros)

##inteiros = []
##for s in numeros:
##    inteiros.append(int(s))
##    print(inteiros)
##
##strings = []
##for n in inteiros:
##    strings.append(str(n))
##    print(strings)


def converte_int(lista):
    inteiros = []
    for s in lista:
        inteiros.append(int(s))
    return inteiros

def converte_str(lista):
    strings = []
    for n in lista:
        strings.append(str(n))
    return strings

def converte(para, lista):
    if para == 'int':
        return converte_int(lista)
    elif para == 'str':
        return converte_str(lista)
    raise TypeError('Tipo de conversão desconhecido')


def maximo(sequencia):
    if not sequencia:
        return None
    maior = sequencia[0]
    for x in sequencia:
        if x > maior:
            maior = x
    return maior


