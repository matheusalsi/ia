from typing import Iterable, Set, Tuple
import re
import copy

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
       


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    print()
    print(estado)
    posicao_underscore = estado.find('_')
    if posicao_underscore != -1:
        print(f"A posição do underscore é: {posicao_underscore}")
    else:
        print("Underscore não encontrado na string.")

    numeros = re.findall(r'\d', estado)
    # Cria uma lista vazia para armazenar os números
    numeros_array = []

    # Adiciona cada número à lista
    for num in numeros:
        numeros_array.append(int(num))
    print(numeros_array)
   
    tupla_sucessor = set()
 
    if(posicao_underscore < 6): 
        # Tupla para "abaixo"
        numeros_array_abaixo = copy.copy(numeros_array)
        numero_indice_4 = numeros_array_abaixo.pop(3)
        numeros_array_abaixo.insert(posicao_underscore, numero_indice_4)
        numeros_array_abaixo .insert(posicao_underscore+3, "_")
        resultado_string = ''.join(map(str, numeros_array_abaixo))
        tupla_sucessor.add(("abaixo", resultado_string))
    else:
        # Tupla para "cima"
        numeros_array_abaixo = copy.copy(numeros_array)
        numero_indice_4 = numeros_array_abaixo.pop(3)
        numeros_array_abaixo.insert(posicao_underscore-1, numero_indice_4)
        numeros_array_abaixo .insert(posicao_underscore-3, "_")
        resultado_string = ''.join(map(str, numeros_array_abaixo))
        tupla_sucessor.add(("acima", resultado_string))

    if(posicao_underscore != 6):
        # Tupla para "esquerda"
        numeros_array_esquerda = copy.copy(numeros_array)
        numeros_array_esquerda.insert(posicao_underscore-1, "_")
        resultado_string = ''.join(map(str, numeros_array_esquerda))
        tupla_sucessor.add(("esquerda", resultado_string))

    # Tupla para "direita"
    numeros_array_direita = copy.copy(numeros_array)
    numeros_array_direita.insert(posicao_underscore+1, "_")
    resultado_string = ''.join(map(str, numeros_array_direita))
    tupla_sucessor.add(("direita", resultado_string))
  
    print(tupla_sucessor)
    return tupla_sucessor


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    nodes = set()
    # Verifica filhos
    successors = sucessor(nodo.estado)
    # Atualiza lista de filhos
    for successor in successors:
        nodes.add(Nodo(successor[1], nodo, successor[0], 1 + nodo.custo))
    return nodes


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
