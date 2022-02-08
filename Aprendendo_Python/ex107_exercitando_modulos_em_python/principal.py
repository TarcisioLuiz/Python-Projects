import moeda

preco = float(input("Digite o preço do produto: "))
print(f'o dobro de R$S{preco} é R${moeda.dobro(preco)}')
print(f'A metade de R$S{preco} é R${moeda.metade(preco)}')
print(f'Aumentando 15% de R$S{preco} será R${moeda.aumentar(preco, 15)}')
print(f'Diminuindo 10% de R$S{preco} será R${moeda.diminuir(preco, 10)}')