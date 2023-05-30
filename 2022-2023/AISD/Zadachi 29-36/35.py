class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def find(self, value):
        current_node = self.root
        while current_node is not None and current_node.value != value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def find_one_child_nodes(self):
        result = []
        stack = [self.root]
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                if node.left is None and node.right is not None:
                    result.append(node)
                elif node.left is not None and node.right is None:
                    result.append(node)
                stack.append(node.left)
                stack.append(node.right)
        return result

binary_tree = BinaryTree()
binary_tree.insert(8)
binary_tree.insert(3)
binary_tree.insert(10)
binary_tree.insert(1)
binary_tree.insert(6)
binary_tree.insert(14)
binary_tree.insert(4)
binary_tree.insert(7)
binary_tree.insert(13)

one_child_nodes = binary_tree.find_one_child_nodes()

for node in one_child_nodes:
    if node.left is None:
        print(f"Node {node.value} has only one child: {node.right.value}")
    else:
        print(f"Node {node.value} has only one child: {node.left.value}")
