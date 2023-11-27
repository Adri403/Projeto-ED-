from meu_grafo_lista_adj import MeuGrafo

grafo = MeuGrafo()

grafo.adiciona_vertice("K")
grafo.adiciona_vertice("J")
grafo.adiciona_vertice("I")
grafo.adiciona_vertice("G")
grafo.adiciona_vertice("H")
grafo.adiciona_vertice("F")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")

grafo.adiciona_aresta("1", "A", "B")
grafo.adiciona_aresta("2", "A", "G")
grafo.adiciona_aresta("3", "A", "J")
grafo.adiciona_aresta("4", "K", "G")
grafo.adiciona_aresta("5", "K", "J")
grafo.adiciona_aresta("6", "J", "G")
grafo.adiciona_aresta("7", "J", "I")
grafo.adiciona_aresta("8", "I", "G")
grafo.adiciona_aresta("9", "H", "G")
grafo.adiciona_aresta("10", "H", "F")
grafo.adiciona_aresta("11", "F", "B")
grafo.adiciona_aresta("12", "B", "G")


arvore = grafo.gerar_todas_arvores("A")

print(arvore)