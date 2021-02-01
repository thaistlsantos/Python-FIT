lista = [1, 5, 7]

cont = 0
for x in lista:
    print(x)
    lista.append(x**2)
    if cont == 10:
        break
    cont += 1


for i in range(len(lista)):
    lista.append(lista[i]**2)
