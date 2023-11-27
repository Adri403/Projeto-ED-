from itertools import product, permutations

dicionario = {'A': ['B', 'G', 'J'], 'B': ['A', 'F', 'G', 'C', 'D', 'E'], 'G': ['A', 'K', 'J', 'I', 'H', 'B'], 'J': ['A', 'K', 'G', 'I'], 'K': ['G', 'J'], 'I': ['J', 'G'], 'H': ['G', 'F'], 'F': ['H', 'B'], 'C': ['B', 'D'], 'D': ['C', 'E', 'B'], 'E': ['D', 'B']}

# Lista para armazenar todos os dicionários possíveis
todos_dicionarios = []
i = 0

# Identificar os vértices com filhos
vertices_com_filhos = {vertice for vertices_filhos in dicionario.values() for vertice in vertices_filhos}

# Gerar todas as permutações possíveis dos valores das chaves
permutacoes_valores = {chave: list(permutations(valores)) if chave in vertices_com_filhos else [valores] for chave, valores in dicionario.items()}

# Gerar todos os dicionários possíveis
for combinacao in product(*permutacoes_valores.values()):
    novo_dicionario = {chave: valores[0] if chave not in vertices_com_filhos else valores for chave, valores in zip(permutacoes_valores.keys(), combinacao)}
    todos_dicionarios.append(novo_dicionario)
    i += 1

# Exibir todos os dicionários gerados
for dicionario_gerado in todos_dicionarios:
    print(dicionario_gerado)

print(i)
