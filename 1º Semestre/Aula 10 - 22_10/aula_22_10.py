def exibir_media():
    m1 = 'Digite um número: '
    m2 = 'Digite outro número: '
    a, b = pedir_numero(m1, m2)
    c = calcular_media(a, b)
    print(c)

def pedir_numero(msg1, msg2):
    msg1 = 'Sobrescrevi'
    n1 = int(input(msg1))
    n2 = int(input(msg2))
    return n1, n2

def calcular_media():
    z = somar(x, y)
    m = z / 2
    return m

def somar(n1, n2):
    s = n1 + n2
    return s


exibir_media()

n1 = int(input())
n2 = int(input())

soma = n1 + n2

media = soma / 2

print(media)