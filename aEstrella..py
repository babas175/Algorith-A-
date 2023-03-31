# Define a função para calcular a distância entre dois pontos
def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

# Define a classe Node para representar cada nó no grafo
class Node:
    def __init__(self, position):
        self.position = position
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.parent = None

    def update_cost(self, g_cost, h_cost):
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

# Define a função para o algoritmo A*
def a_star(start, end, graph):
    # Cria os nós iniciais e finais
    start_node = Node(start)
    end_node = Node(end)

    # Inicializa a lista de nós abertos e fechados
    open_list = [start_node]
    closed_list = []

    # Loop até encontrar o caminho final ou até que a lista de nós abertos esteja vazia
    while open_list:
        # Seleciona o nó com o menor f_cost
        current_node = min(open_list, key=lambda x: x.f_cost)

        # Remove o nó atual da lista de nós abertos e adiciona na lista de nós fechados
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Se o nó atual é o nó final, retorna o caminho
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Gera os filhos do nó atual
        for child_pos in graph[current_node.position]:
            child_node = Node(child_pos)
            child_g_cost = current_node.g_cost + distance(current_node.position, child_pos)
            child_h_cost = distance(child_pos, end_node.position)
            child_node.update_cost(child_g_cost, child_h_cost)
            child_node.parent = current_node

            # Se o filho já estiver na lista de nós fechados, continue
            if child_node in closed_list:
                continue

            # Se o filho não estiver na lista de nós abertos, adiciona na lista
            if child_node not in open_list:
                open_list.append(child_node)
            # Se o filho já estiver na lista de nós abertos, verifica se esse caminho é melhor que o anterior
            else:
                existing_node = open_list[open_list.index(child_node)]
                if child_node.g_cost < existing_node.g_cost:
                    existing_node.update_cost(child_node.g_cost, child_node.h_cost)
                    existing_node.parent = child_node.parent

    # Se não encontrar um caminho, retorna None
    return None
