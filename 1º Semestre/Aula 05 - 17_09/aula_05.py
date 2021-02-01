n = int(input())

# estrutura de seleção simples
# executamos um trecho de código apenas se
# a condição for verdadeira
if n == 0:
    print('n é igual a zero')

# estrutura de seleção composta
# temos apenas 1 condição, mas 2 caminhos:
# 	ou n é maior
# 	ou n não é maior (o que inclui ser igual)

if n > 10:      # se
    print('n é maior que 10')
    print('bloco dentro do if')
else:           # senão
    print('n NÃO é maior que 10')
    print('bloco dentro do else')

print('fim')


#### seleção simples
##se <condição>:
##    <bloco de código>
##
##<bloco fora do if>
##
##
#### seleção composta
##se <condição>:
##    <bloco de código>
##senão:
##    <bloco de código>
##
##<bloco fora do if>

