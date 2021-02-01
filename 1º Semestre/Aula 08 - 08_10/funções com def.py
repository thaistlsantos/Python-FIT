def somar(a, b):
    s = a + b
    return s

def exibe_soma(valor):
    saida = 'A soma é {}'.format(valor)
    print(saida)

resultado = somar(3, 8)

exibe_soma(resultado)
