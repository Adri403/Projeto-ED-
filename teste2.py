from meu_grafo_lista_adj import MeuGrafo

'''
g_p = MeuGrafo()
g_p.adiciona_vertice("J")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("E")
g_p.adiciona_vertice("P")
g_p.adiciona_vertice("M")
g_p.adiciona_vertice("T")
g_p.adiciona_vertice("Z")
g_p.adiciona_aresta('a1', 'J', 'C')
g_p.adiciona_aresta('a2', 'C', 'E')
g_p.adiciona_aresta('a3', 'C', 'E')
g_p.adiciona_aresta('a4', 'P', 'C')
g_p.adiciona_aresta('a5', 'P', 'C')
g_p.adiciona_aresta('a6', 'T', 'C')
g_p.adiciona_aresta('a7', 'M', 'C')
g_p.adiciona_aresta('a8', 'M', 'T')
g_p.adiciona_aresta('a9', 'T', 'Z')

todas_arvores = g_p.gerar_todas_arvores("J")

for c in todas_arvores:
    print(c)
    print('')

'''

# Grafos completos
g_c = MeuGrafo()
g_c.adiciona_vertice("J")
g_c.adiciona_vertice("C")
g_c.adiciona_vertice("E")
g_c.adiciona_vertice("P")
g_c.adiciona_aresta('a1', 'J', 'C')
g_c.adiciona_aresta('a2', 'J', 'E')
g_c.adiciona_aresta('a3', 'J', 'P')
g_c.adiciona_aresta('a4', 'E', 'C')
g_c.adiciona_aresta('a5', 'P', 'C')
g_c.adiciona_aresta('a6', 'P', 'E')

todas_arvores = g_c.gerar_todas_arvores("J")

for g in todas_arvores:
    print(g)
    print('')

'''
g_c2 = MeuGrafo()
g_c2.adiciona_vertice("Nina")
g_c2.adiciona_vertice("Maria")
g_c2.adiciona_vertice("Joana")
g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')
g_c2.adiciona_aresta('amiga2', 'Nina', 'Joana')
g_c2.adiciona_aresta('amiga3', 'Joana', 'Maria')

arvores_g_c2 = g_c2.gerar_todas_arvores("Nina")

for k in arvores_g_c2:
    print(k)
    print('')


g_c3 = MeuGrafo()
g_c3.adiciona_vertice("Único")

arvore_g_c3 = g_c3.gerar_todas_arvores("Único")
for c in arvore_g_c3:
    print(c)
    print('')


# Grafos com laco
g_l1 = MeuGrafo()
g_l1.adiciona_vertice("A")
g_l1.adiciona_vertice("B")
g_l1.adiciona_vertice("C")
g_l1.adiciona_vertice("D")
g_l1.adiciona_aresta('a1', 'A', 'A')
g_l1.adiciona_aresta('a2', 'A', 'B')
g_l1.adiciona_aresta('a3', 'A', 'A')

todas_arvores_g_l1 = g_l1.gerar_todas_arvores("A")

for c in todas_arvores_g_l1:
    print(c)
    print('')



g_l2 = MeuGrafo()
g_l2.adiciona_vertice("A")
g_l2.adiciona_vertice("B")
g_l2.adiciona_vertice("C")
g_l2.adiciona_vertice("D")
g_l2.adiciona_aresta('a1', 'A', 'B')
g_l2.adiciona_aresta('a2', 'B', 'B')
g_l2.adiciona_aresta('a3', 'B', 'A')

arvore_g_l2 = g_l2.dfs("B")
print(arvore_g_l2)


# Grafos desconexos
g_d = MeuGrafo()
g_d.adiciona_vertice("A")
g_d.adiciona_vertice("B")
g_d.adiciona_vertice("C")
g_d.adiciona_vertice("D")
g_d.adiciona_aresta('asd', 'A', 'B')

arvore_g_d = g_d.dfs("A")


print(arvore_g_d)
g_d2 = MeuGrafo()
g_d2.adiciona_vertice("A")
g_d2.adiciona_vertice("B")
g_d2.adiciona_vertice("C")
g_d2.adiciona_vertice("D")

arvore_g_d2 = g_d2.dfs("D")

print(arvore_g_d2)

'''

