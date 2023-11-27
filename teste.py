from meu_grafo_lista_adj import MeuGrafo


g_p = MeuGrafo()
g_p.adiciona_vertice("J")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("E")
g_p.adiciona_vertice("P")
g_p.adiciona_vertice("M")
g_p.adiciona_vertice("T")
g_p.adiciona_vertice("Z")
g_p.adiciona_aresta("a1", "J", "C")
g_p.adiciona_aresta("a2", "C", "E")
g_p.adiciona_aresta("a3", "C", "E")
g_p.adiciona_aresta("a4", "C", "P")
g_p.adiciona_aresta("a5", "C", "P")
g_p.adiciona_aresta("a6", "C", "M")
g_p.adiciona_aresta("a7", "C", "T")
g_p.adiciona_aresta("a8", "M", "T")
g_p.adiciona_aresta("a9", "T", "Z")

todas_arvores = g_p.gerar_todas_arvores("Z")

for c in todas_arvores:
    print(c)

