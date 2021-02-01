## Exibir todos os números PARES de 0 até n

n = int(input("digite o n:"))

print('sem o if...')
cont1 = 0
while cont1 <= n:
    print(cont2)
    cont1 = cont1 + 2

print()
print('com o if...')
cont2 = 0
while cont2 <= n:
    if cont2 % 2 == 0:
        print(cont2)
    cont2 = cont2 + 1
