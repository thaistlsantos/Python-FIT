soma = 0

cont = 1

while soma <= 21:
    mensagem = 'Digite o {} numero: '.format(cont)
    num = int(input(mensagem))
    soma = soma + num

print('A soma dos números é: ', soma)
