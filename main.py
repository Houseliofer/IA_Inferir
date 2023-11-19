class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_path(root):
    max_path = 0
    max_path_list = []

    def dfs(node, current_path):
        if node is None:
            return

        current_path.append(node.value)

        # chequear si este camino es mayor que el maximo actual
        current_path_sum = sum(current_path)
        nonlocal max_path, max_path_list
        if current_path_sum > max_path:
            max_path = current_path_sum
            max_path_list = list(current_path)

        # seguir dfs 
        dfs(node.left, current_path)
        dfs(node.right, current_path)

        # retroceder
        current_path.pop()

    dfs(root, [])
    return max_path, max_path_list


# construir el árbol a partir de la entrada del usuario

print("Ingrese los nodos del árbol level-order, separados por espacios:")
values = list(map(int, input().split()))

root = Node(values[0])
nodes = [root]

for i in range(1, len(values), 2):
    left_val, right_val = values[i], values[i + 1]
    left_node = Node(left_val)
    right_node = Node(right_val)

    nodes[0].left = left_node
    nodes[0].right = right_node

    nodes.append(left_node)
    nodes.append(right_node)
    nodes = nodes[1:]

print()
print(find_max_path(root))
# ejemplo de uso
#root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
#root.right.left = Node(6)
#root.right.right = Node(7)

#          1
#        /   \
#      2       3
#    /   \    /  \
#  4      5  6    7
#
#print(find_max_path(root))

# (11, [1, 3, ,7])