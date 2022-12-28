from typing import List
from collections import deque

class Node:
    def __init__(self):
        self.connections: List[Node] = []
        self.number = 0

def bfs(node: Node, search_number):
    global search_node, found_number

    visited = []
    frontier = deque()
    frontier.append(node)

    while len(frontier) != 0:
        node = frontier.popleft()

        if node in visited:
            continue

        if node.number == search_number:
            return node

        visited.append(node)

        for next_node in node.connections:
            frontier.append(next_node)
    return None


head_node = Node()
head_node.number = 0

node = Node()
head_node.connections.append(node)
node = Node()
node.number = 10
head_node.connections.append(node)

print(bfs(head_node, 10))