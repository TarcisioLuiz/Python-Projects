import moeda

preco = float(input("Digite o preço do produto: "))
format = str(input("Deseja que os valores sejam formatados em dobro: [S/N] ")).upper()
print(f'o dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, format)}')

format = str(input("Deseja que os valores sejam formatados em metade: [S/N] ")).upper()
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, format)}')

format = str(input("Deseja que os valores sejam formatados em aumento: [S/N] ")).upper()
print(f'Aumentando 15% de {moeda.moeda(preco)} será {moeda.aumentar(preco, 15, format)}')

format = str(input("Deseja que os valores sejam formatados em diminuição: [S/N] ")).upper()
print(f'Diminuindo 10% de {moeda.moeda(preco)} será {moeda.diminuir(preco, 10, format)}')