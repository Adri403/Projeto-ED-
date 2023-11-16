from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_lista_adj import MeuGrafo

grafo = GrafoListaAdjacencia()
arestas = grafo.arestas

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
grafo.adiciona_aresta("13", "B", "C")
grafo.adiciona_aresta("14", "C", "D")
grafo.adiciona_aresta("15", "D", "E")
grafo.adiciona_aresta("16", "D", "B")
grafo.adiciona_aresta("17", "E", "B")




for c in MeuGrafo.dfs(grafo, "E", list(), list()):
    print(str(arestas[c])[:7])
 