lista = [5, 25, 39]
print(id(lista))
lista2 = [2, 3]
lista.extend(lista2)
print(id(lista))
lista.extend(['a', True])
print(id(lista))

print()

tupla = (5, 25, 39)
print(id(tupla))
tupla2 = (2, 3)
tupla_reserva1 = tupla
tupla = tupla + tupla2
print(id(tupla))
tupla_reserva2 = tupla
tupla = tupla + ('a', True)
print(id(tupla))

#lista.pop(3)
