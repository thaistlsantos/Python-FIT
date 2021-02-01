# Funções

def tamanho(sequencia):
    cont = 0
    for _ in sequencia:
        cont += 1
    return cont

def contar(sequencia, valor):
    cont = 0
    for x in sequencia:
        if x == valor:
            cont += 1
    return cont

def somar(sequencia):
    soma = 0
    for x in sequencia:
        soma += x
    return soma

def all_indexes(sequencia, valor):
    """
    Retorna uma lista com todos os índices de <valor> encontrados em <sequência>

    Se não for encontrado nenhum, retorna uma lista vazia []
    """
    pass


# Código principal

lista = [2, 3, 25, 4, 87, 27, 25]

n1_lista = tamanho(lista)
n2_lista = len(lista)

print(n1_lista, n2_lista)
