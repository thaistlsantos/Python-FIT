def soma():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    s = n1 + n2

    print(s)
    return 

print('fim da função! (primeira linha fora da função)')

print('chamando a função...')
soma()

print('chamando novamente a função...')
soma()

"""
Exercício:
Receber o valor de uma compra e a opção
relativa a forma de pagamento.
-------------------------------------------------------------
 | Opção |                Forma de pagamento               |
- ------- ------------------------------------------------- -
 |   1   | A vista em dinheiro - 10% de desconto           |
 |   2   | A vista no cartão   - 5% de desconto            |   
 |   3   | Em 2x no cartão     - Sem desconto e sem juros  |
 |   4   | Em 5x no cartão     - 10% de juros              |
-------------------------------------------------------------
Exibir o valor total a pagar (com juros ou desconto),
o número de parcelas e o valor de cada parcela
"""
    
#0  1   2   3
if opcao == 1:
    # dar 10% de desconto
else:
    # sei que não é 1
    if opcao == 2:
        # dar 5% de desconto
    else:
        # sei que não é 1 nem 2
        if opcao == 3:
            # preço normal em 2x
        else:
            # sei que não é 1, nem 2 e nem 3
            # cobrar 10% de juros e
            # parcelar em 5x
