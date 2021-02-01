
# entradas
km = int(input('digite os km: '))
dias = int(input('digite os dias: '))

# processamento
preco_km = 0.15 * km
preco_dias = 60 * dias

preco_total = preco_km + preco_dias

# exibição do resultado
print('Custo total é R$ {:.2f}'.format(preco_total))
