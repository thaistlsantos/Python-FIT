##Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
##metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
##para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$
##80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço
##total.

# 1) vi quais são as informações importantes
# 2) pensei sobre como resolver o problema
#       2.1) dividi o problema em partes menores
# 3) escrevi o código

# importação do módulo no começo do código (apenas 1 vez)
import math

## pedir área em metros quadrados
area = int(input('Digite a area: '))

## 1 litro cobre 3 metros quadrados, quantos litros preciso?
litros  = area / 3

## 1 lata tem 18 litros, quantas latas preciso?
latas = math.ceil(litros / 18)

## 1 lata custa R$ 80,00
custo = 80 * latas

## Exibir número de latas e preço final
saida = 'Compre {} latas, no preço de R$ {:.2f}'.format(latas, custo)

print(saida)

