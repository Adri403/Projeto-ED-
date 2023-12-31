from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        arestas = self.arestas
        vertices = self.vertices
        dict_adjacentes = dict()

        for k in arestas:
            v1 = str(arestas[k].v1)
            v2 = str(arestas[k].v2)

            if v1 not in dict_adjacentes:
                dict_adjacentes[v1] = []

            if v2 not in dict_adjacentes[v1]:
                dict_adjacentes[v1].append(v2)

            if v2 not in dict_adjacentes:
                dict_adjacentes[v2] = []

            if v1 not in dict_adjacentes[v2]:
                dict_adjacentes[v2].append(v1)
        
        vertices_nao_adjacentes = set()

        for v1 in vertices:
            for v2 in vertices:
                v1 = str(v1)
                v2 = str(v2)

                if v1 not in dict_adjacentes and v2 not in dict_adjacentes:
                    par = f"{v1}-{v2}"
                    inverso = f"{v2}-{v1}"
                    if par not in vertices_nao_adjacentes and inverso not in vertices_nao_adjacentes and v1 != v2:
                            vertices_nao_adjacentes.add(par)
                    

                if v1 in dict_adjacentes:
                    if v1 != v2 and v2 not in dict_adjacentes[v1]:
                        par = f"{v1}-{v2}"
                        inverso = f"{v2}-{v1}"

                        if par not in vertices_nao_adjacentes and inverso not in vertices_nao_adjacentes:
                            vertices_nao_adjacentes.add(par)


        return vertices_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        arestas = self.arestas

        for lista in range(len(arestas)):
           for dicionario in range(len(arestas[lista])):
                if arestas[lista][dicionario] == {}:
                    continue
                else:
                    for chave in arestas[lista][dicionario]:
                        if arestas[lista][dicionario][chave].v1 == arestas[lista][dicionario][chave].v2:
                            return True
        
        return False
           

    def grau(self, V):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        arestas = self.arestas
        vertices = self.vertices
        vertices_string = list()
        grau = 0

        for c in range(len(vertices)):
            vertices_string.append(str(vertices[c]))

        if V in vertices_string:
            for k in arestas:
                if V == str(arestas[k].v1) and V == str(arestas[k].v2):
                    grau += 2
                elif V == str(arestas[k].v1) or V == str(arestas[k].v2):
                    grau += 1

            return grau
        else:
            raise VerticeInvalidoError()
        

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas = self.arestas

        for k in arestas:
            for l in arestas:
                if k == l:
                    continue
                else:
                    if (arestas[k].v1 == arestas[l].v1 and arestas[k].v2 == arestas[l].v2) or (arestas[k].v1 == arestas[l].v2 and arestas[k].v2 == arestas[l].v1):
                        return True
                    
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas = self.arestas
        vertices = self.vertices
        vertices_string = list()
        lista_arestas = set()

        for c in range(len(vertices)):
            vertices_string.append(str(vertices[c]))

        if V in vertices_string:
            for k in arestas:
                if V == str(arestas[k].v1) or V == str(arestas[k].v2):
                    lista_arestas.add(k)

            return lista_arestas
        else:
            raise VerticeInvalidoError()
            

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        arestas = self.arestas
        vertices = self.vertices
        dict_adjacentes = dict()

        if len(vertices) == 1 and MeuGrafo.ha_laco(self):
            return False
        elif len(vertices) == 2 and MeuGrafo.ha_laco(self):
            return False
        elif len(vertices) > 1 and len(arestas) == 0:
            return False

        for k in arestas:
            v1 = str(arestas[k].v1)
            v2 = str(arestas[k].v2)

            if v1 not in dict_adjacentes:
                dict_adjacentes[v1] = []

            if v2 not in dict_adjacentes[v1]:
                dict_adjacentes[v1].append(v2)

            if v2 not in dict_adjacentes:
                dict_adjacentes[v2] = []

            if v1 not in dict_adjacentes[v2]:
                dict_adjacentes[v2].append(v1)

        for v in vertices:
            for d in dict_adjacentes:
                if str(v) != d and str(v) not in dict_adjacentes[d]:
                    return False
        return True