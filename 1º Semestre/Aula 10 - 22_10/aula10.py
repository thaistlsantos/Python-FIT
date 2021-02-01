n = 5

soma = 0
i = 1
while i <= n:
    print(i)
    termo = i
    soma = soma + termo
    
    i = i + 1

print(soma)


########
texto = 'abcd'

novo_texto = ''
for letra in texto:
    if letra == 'c':
        novo_texto = novo_texto + 'X'
    else:
        novo_texto = novo_texto + letra
    print(novo_texto)
