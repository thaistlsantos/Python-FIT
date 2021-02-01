def bem_vindo():
    print('Seja bem vindo!')

def retorna_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media
   
bem_vindo()
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

resposta_1 = retorna_media(a, b, c)

resposta_2 = retorna_media(1, 2, 4)

resposta_3 = retorna_media(c, b, a)  

print('A média 1 é:', resposta_1)
print('A média 2 é:', resposta_2)
print('A média 3 é:', resposta_3)
