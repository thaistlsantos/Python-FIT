lista = [1, 5, 7, 6, 9]

for x in lista:
    print(x)
    lista.append(x**2)
    if cont == 10:
        break
    cont += 1

n = len(lista)
for i in range(len(lista)):
    lista.append(lista[i] ** 2)
