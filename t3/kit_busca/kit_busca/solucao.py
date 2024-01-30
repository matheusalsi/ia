from typing import Set, Tuple
import re
import copy
from heapq import heapify, heappush, heappop
# define o estado final do game
ESTADO_FINAL = "12345678_"
# monta matriz do board final do game
BOARD_FINAL_INDEXES = {'1' : [0,0], '2' : [1,0], '3' : [2,0],
                       '4' : [0,1], '5' : [1,1], '6' : [2,1],
                       '7' : [0,2], '8' : [1,2], '_' : [2,2]}

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.custo_estimado = 0

    def __lt__(self, nxt):
        return self.custo_estimado < nxt.custo_estimado
       

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    posicao_underscore = estado.find('_')

    numeros = re.findall(r'\d', estado)

    # Cria uma lista vazia para armazenar os números
    numeros_array = []

    # Adiciona cada número à lista
    for num in numeros:
        numeros_array.append(int(num))
   
    tupla_sucessor = set()

    if(posicao_underscore - 3 >= 0):
        # para "cima"
        sl = list(estado)
        sl[posicao_underscore], sl[posicao_underscore - 3] = sl[posicao_underscore - 3], sl[posicao_underscore]
        tupla_sucessor.add(("acima", ''.join(sl)))
 
    if(posicao_underscore + 3 <= 8): 
        # para "abaixo"
        sl = list(estado)
        sl[posicao_underscore], sl[posicao_underscore + 3] = sl[posicao_underscore + 3], sl[posicao_underscore]
        tupla_sucessor.add(("abaixo", ''.join(sl)))

    if(posicao_underscore + 1) % 3 != 0:
        # para "direita"
        numeros_array_direita = copy.copy(numeros_array)
        numeros_array_direita.insert(posicao_underscore+1, "_")
        resultado_string = ''.join(map(str, numeros_array_direita))
        tupla_sucessor.add(("direita", resultado_string))

    if(posicao_underscore % 3 != 0):
        # para "esquerda"
        numeros_array_esquerda = copy.copy(numeros_array)
        numeros_array_esquerda.insert(posicao_underscore-1, "_")
        resultado_string = ''.join(map(str, numeros_array_esquerda))
        tupla_sucessor.add(("esquerda", resultado_string))

    return tupla_sucessor


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    nodes = set()
    successors = sucessor(nodo.estado)
    for successor in successors:
        nodes.add(Nodo(successor[1], nodo, successor[0], 1 + nodo.custo))
    return nodes

def findPath(node: Nodo) -> list[str]:
    path = []
    while(node.pai is not None):
        path.insert(0, node.acao)
        node = node.pai
    return path
            
def hamming(node_state: str) -> int:
    hamming_cost = 0
    for i in range(len(ESTADO_FINAL)):
        if node_state[i] != ESTADO_FINAL[i]:
            hamming_cost += 1
    return hamming_cost

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    nodo_inicial = Nodo(estado, None, None, 0)
    already_explored = set()
    fronteira = [nodo_inicial]
    heapify(fronteira)
    
    while (fronteira):
        # remove o nodo com o menor custo estimado da heap
        current_node = heappop(fronteira) 
        
        if current_node.estado == ESTADO_FINAL:
            return findPath(current_node)
        if current_node.estado not in  already_explored:
            already_explored.add(current_node.estado)
            expandedNodes = expande(current_node)
            for node in expandedNodes:
                node.custo_estimado = node.custo + hamming(node.estado)
                heappush(fronteira, node)
    return None
    
def manhattan(node_state: str) -> int:    
    puzzleBoard = {}
    for i in range(len(ESTADO_FINAL)):
         puzzleBoard[node_state[i]] = [i % 3, i // 3]
        
    manhattanCost = 0
    for key in puzzleBoard.keys():
        manhattanCost += (BOARD_FINAL_INDEXES[key][0] - puzzleBoard[key][0]) + (BOARD_FINAL_INDEXES[key][1] - puzzleBoard[key][1])
    
    return manhattanCost

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    nodo_inicial = Nodo(estado, None, None, 0)
    already_explored = set()
    fronteira = [nodo_inicial]
    heapify(fronteira)
    
    while (fronteira):
        # remove o nodo com o menor custo estimado da heap
        current_node = heappop(fronteira) 
        
        if current_node.estado == ESTADO_FINAL:
            return findPath(current_node)
        if current_node.estado not in  already_explored:
            already_explored.add(current_node.estado)
            expandedNodes = expande(current_node)
            for node in expandedNodes:
                node.custo_estimado = node.custo + manhattan(node.estado)
                heappush(fronteira, node)
    return None

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
