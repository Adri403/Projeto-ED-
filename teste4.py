from itertools import permutations, product

# Seu dicionário
dicionario = {'A': ['B', 'G', 'J'], 'B': ['A', 'F', 'G', 'C', 'D', 'E'], 'G': ['A', 'K', 'J', 'I', 'H', 'B'], 'J': ['A', 'K', 'G', 'I'], 'K': ['G', 'J'], 'I': ['J', 'G'], 'H': ['G', 'F'], 'F': ['H', 'B'], 'C': ['B', 'D'], 'D': ['C', 'E', 'B'], 'E': ['D', 'B']}
i = 0
# Lista para armazenar todos os dicionários possíveis
todos_dicionarios = []

# Gerar todas as permutações possíveis dos valores das chaves
permutacoes_valores = {chave: list(permutations(valores)) for chave, valores in dicionario.items()}

# Gerar todos os dicionários possíveis
for combinacao in product(*permutacoes_valores.values()):
    novo_dicionario = {chave: valores for chave, valores in zip(permutacoes_valores.keys(), combinacao)}
    todos_dicionarios.append(novo_dicionario)
    

# Exibir todos os dicionários gerados
for dicionario_gerado in todos_dicionarios:
    print(dicionario_gerado)
    i += 1

print(i)