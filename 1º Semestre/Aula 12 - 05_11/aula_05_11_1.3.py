entrada = '1 2 3 5 6 9 7 '

#split
numeros = entrada.split()
print(numeros)

#trás um item de lista em inteiros em uma posição
# int(numeros)
# int(numeros[1])

inteiros = []
for s in numeros:
    inteiros.append(int(s))
    print(inteiros)

strings = []
for n in inteiros:
    strings.append(str(n))
    print(strings)






