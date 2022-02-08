import moeda

preco = float(input("Digite o preço do produto: "))
print(f'o dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}')
print(f'Aumentando 15% de {moeda.moeda(preco)} será {moeda.aumentar(preco, 15)}')
print(f'Diminuindo 10% de {moeda.moeda(preco)} será {moeda.diminuir(preco, 10)}')