"""
Listas, dicionarios, sets
"""

# Agora vamos explorar uma das principais estruturas do Python, as listas
compras = ['laranja', 'cafe']

# podemos checar o tamanho da lista
print(len(compras))

# Agora podemos percorrer a lista
for i in compras:
    print(i)

# Gera um lista com intervalo [0,..10]
elementos_10 = []
for i in range(10):
    print(i)
    elementos_10.append(i)

# Gerando uma lista em uma única linha [ 0, 1, 2, .. 10]
lista_uma_linha = [i for i in range(10)]

# Dicionario
carrinho = {"laranja": 2.0, "cafe": 5.0}

for i in carrinho:
    print(carrinho[i])

# Chave, valor
for chave, valor in carrinho.items():
    print(f"chave:{chave} valor{valor}")

# Chaves do dicionario
print(f"Chaves dicionario: {carrinho.keys()}")

# Adicionar um novo item no dicionário
carrinho['leite'] = 5

print(f"Agora vamos exibir os items no dicionário {carrinho}")