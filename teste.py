from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_lista_adj import MeuGrafo

paraiba = GrafoListaAdjacencia()

paraiba.adiciona_vertice("J")
paraiba.adiciona_vertice("C")
paraiba.adiciona_vertice("E")
paraiba.adiciona_vertice("P")
paraiba.adiciona_vertice("M")
paraiba.adiciona_vertice("T")
paraiba.adiciona_vertice("Z")

paraiba.adiciona_aresta('a1', 'J', 'C')
paraiba.adiciona_aresta('a2', 'C', 'E')
paraiba.adiciona_aresta('a3', 'C', 'Z')
paraiba.adiciona_aresta('a4', 'C', 'M')
paraiba.adiciona_aresta('a5', 'C', 'P')
paraiba.adiciona_aresta('a6', 'C', 'M')
paraiba.adiciona_aresta('a7', 'C', 'T')
paraiba.adiciona_aresta('a8', 'M', 'T')
paraiba.adiciona_aresta('a9', 'T', 'Z')

print(MeuGrafo.vertices_nao_adjacentes(paraiba))
print(*MeuGrafo.ha_laco(paraiba))
print(*MeuGrafo.ha_paralelas(paraiba))
print(*MeuGrafo.eh_completo(paraiba))

V = input()

print(MeuGrafo.grau(paraiba, V))
print(MeuGrafo.arestas_sobre_vertice(paraiba, V))