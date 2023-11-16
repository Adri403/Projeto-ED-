from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        vertices = self.vertices

        # Cria um dicionário de vértices em que cada chave possui uma lista de vértices adjacentes a ela
        dict_adjacentes = MeuGrafo.vertices_adjacentes(self)
        
        vertices_nao_adjacentes = set()
        
        for v1 in vertices:
            for v2 in vertices:
                v1 = str(v1)
                v2 = str(v2)

                # Verifica se o vértice 1 e 2 está no dicionário. Caso contrário, forma um par de vértices não adjacentes
                if v1 not in dict_adjacentes and v2 not in dict_adjacentes:
                    par = f"{v1}-{v2}"
                    inverso = f"{v2}-{v1}"
                    # Se o par ou o inverso das extremidades da aresta não estiver no set de vértices não adjacentes, então adiciona o par
                    if par not in vertices_nao_adjacentes and inverso not in vertices_nao_adjacentes and v1 != v2:
                            vertices_nao_adjacentes.add(par)
                    
                # Verifica se o vértice 1 está no dicionário e se vértice 2(que deve ser diferente do 1) está dentro da lista da chave(vértice 1)
                if v1 in dict_adjacentes:
                    # Caso sim, forma um par de vértices não adjacentes
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

        # Verifica se os vértices da arestas são iguais
        for x in arestas:
            if arestas[x].v1 == arestas[x].v2:
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

        # Verifica se o vértice está no grafo
        if V in vertices_string:
            for k in arestas:
                v1 = str(arestas[k].v1)
                v2 = str(arestas[k].v2)

                # Verifica se vértices v1 e v2 da aresta são iguais ao vértice V
                if V == v1 and V == v2:
                    grau += 2
                # Verifica se um dos vértices da aresta são iguais ao vértice V
                elif V == v1 or V == v2:
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

        # Percorre o dicionário de arestas.
        for k in arestas:
            # Percorre o dicionário também, mas arestas l devem diferentes de k.
            for l in arestas:
                if k == l:
                    continue
                else:
                    # Verifica se os vértices da aresta k são iguais aos da aresta l
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
        set_arestas = set()

        for c in range(len(vertices)):
            vertices_string.append(str(vertices[c]))

        if V in vertices_string:
            # Percorre o dicionário de arestas
            for k in arestas:
                # Verifica se o vértice V é igual a pelo menos um dos vértices da aresta analisada
                if str(V) == str(arestas[k].v1) or str(V) == str(arestas[k].v2):
                    set_arestas.add(k)

            return set_arestas
        else:
            raise VerticeInvalidoError()
            

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        arestas = self.arestas
        vertices = self.vertices

        # Cria um dicionário de vértices em que cada chave possui uma lista de vértices adjacentes a ela
        dict_adjacentes = MeuGrafo.vertices_adjacentes(self)

        # Se o grafo possui um vértice com laço, então retorna falso
        if len(vertices) == 1 and MeuGrafo.ha_laco(self):
            return False
        # Mesma coisa aqui, mas com um grafo de 2 vértices
        elif len(vertices) == 2 and MeuGrafo.ha_laco(self):
            return False
        # Se o grafo possuir vértices e não possuir arestas, então retorna falso
        elif len(vertices) > 1 and len(arestas) == 0:
            return False
        
        # Cria um dicionário de vértices em que cada chave possui uma lista de vértices adjacentes a ela
        dict_adjacentes = MeuGrafo.vertices_adjacentes(self)

        for v in vertices:
            for d in dict_adjacentes:
                # Verifica se o vértice v não está na lista de adjacentes a chave
                if str(v) != d and str(v) not in dict_adjacentes[d]:
                    return False
        return True
    


    
    def dfs(self, V, vertices_visitados, arvore):
        
        # Variável "grafo" recebe um dicionário de chaves(vértices) em que seus valores são listas dos vértices adjacentes a ele
        grafo = MeuGrafo.vertices_adjacentes(self)
        arestas = self.arestas
        
        # Se vértice não estiver na lista de visitados, adicione-o
        if V not in vertices_visitados:
            vertices_visitados.append(V)
            
            # Percorre a lista de adjacentes da chave(vértice)
            for vizinho in grafo[V]:
                # Verifica se o vizinho não está na lista de visitados 
                if vizinho not in vertices_visitados:
                    # Percorre as arestas para poder pegar a aresta que tem os vértices "V" e "vizinho" nas extremidades
                    for ars in arestas:
                        # Verifica se essa formatação "V-vizinho" está igual a uma das arestas do grafo
                        if f'{V}-{vizinho}' == str(arestas[ars])[3:6] or f'{vizinho}-{V}' == str(arestas[ars])[3:6] or f'{V}-{vizinho}' == str(arestas[ars])[2:5] or f'{vizinho}-{V}' == str(arestas[ars])[2:5]:
                            arvore.append(ars)
                            break
                    MeuGrafo.dfs(self, vizinho, vertices_visitados, arvore)

        return arvore
            
            
    def vertices_adjacentes(self):

        arestas = self.arestas
        dict_adjacentes = dict()

        # Percorre o dicionário de arestas
        for k in arestas:
            # Variáveis recebem os vértices da aresta
            v1 = str(arestas[k].v1)
            v2 = str(arestas[k].v2)

            # Se v1 não estiver no dicionário de adjacentes, então adiciona-o
            if v1 not in dict_adjacentes:
                dict_adjacentes[v1] = list()

            # Se v2 não estiver dentro da lista de adjacentes ao v1, então adiciona na lista do v1
            if v2 not in dict_adjacentes[v1]:
                dict_adjacentes[v1].append(v2)

            # Mesma coisa aqui, mas com o segundo vértice
            if v2 not in dict_adjacentes:
                dict_adjacentes[v2] = list()

            # Mesma coisa do "if v2 not in dict_adjacentes[v1]", mas o contrário
            if v1 not in dict_adjacentes[v2]:
                dict_adjacentes[v2].append(v1)

        return dict_adjacentes