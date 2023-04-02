import math

class Node:
    def __init__(self, pos):
        self.pos = pos
        self.adj = []
        self.g = math.inf
        self.h = 0

def heuristic(a, b):
    return math.sqrt((b.pos[0] - a.pos[0]) ** 2 + (b.pos[1] - a.pos[1]) ** 2)

def astar(start, end):
    open_list = [start]
    closed_list = []

    start.g = 0
    start.h = heuristic(start, end)

    while len(open_list) > 0:
        current = min(open_list, key=lambda x: x.g + x.h)

        if current == end:
            path = []
            while current != start:
                path.append(current.pos)
                current = current.parent
            path.append(start.pos)
            return path[::-1]

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in current.adj:
            if neighbor in closed_list:
                continue

            tentative_g = current.g + heuristic(current, neighbor)
            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= neighbor.g:
                continue

            neighbor.g = tentative_g
            neighbor.h = heuristic(neighbor, end)
            neighbor.parent = current

    return None

def main():
    n1 = Node((0, 0))
    n2 = Node((1, 1))
    n3 = Node((2, 2))
    n4 = Node((3, 3))

    n1.adj