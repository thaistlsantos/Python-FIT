# Jogo de 21 ou Black Jack

# importações
import random

# Funções

# Código principal

# Flags
perdeu = False
continuar = True


soma = 0
cont = 1

while not perdeu and continuar:

    carta = random.randint(1, 10)
    soma = soma + carta

    print('{}a carta, pontuação: {}'.format(cont, soma))
    
    if soma > 21:
        perdeu = True
    else:
        resposta = input('Mais uma carta? (s/n) ')
        if resposta == 'n' or resposta == 'não':
            continuar = False
        else:
            cont = cont + 1

if perdeu:
    print('Você perdeu!')
elif soma == 21:
    print('Black Jack!')
else:
    print('Você tem {} pontos, faltam {}'
          .format(soma, 21-soma))
