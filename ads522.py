from typing import List

class Node:
    def __init__(self):
        self.connections: List[Node] = []
        self.visited = False
        self.number = 0


search_node = Node
found_number = False

def dfs(node: Node, search_number):
    global search_node, found_number

    if found_number:
        return

    node.visited = True

    if node.number == search_number:
        found_number = True
        search_node = node
        return

    for next_node in node.connections:
        if next_node.visited:
            continue
        else:
            dfs(next_node, search_number)

head_node = Node()
head_node.number = 0

node = Node()
head_node.connections.append(node)
node = Node()
node.number = 10
head_node.connections.append(node)

dfs(head_node, 10)

if found_number:
    print(node.number)