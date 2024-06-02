class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if key > node.val:
                if node.right is None:
                    node.right = TreeNode(key)
                else:
                    self._insert(node.right, key)

    def pre_order_traversal(self, node, stack):
        if node:
            stack.push(node.val)
            self.pre_order_traversal(node.left, stack)
            self.pre_order_traversal(node.right, stack)

    def in_order_traversal(self, node, stack):
        if node:
            self.in_order_traversal(node.left, stack)
            stack.push(node.val)
            self.in_order_traversal(node.right, stack)

    def post_order_traversal(self, node, stack):
        if node:
            self.post_order_traversal(node.left, stack)
            self.post_order_traversal(node.right, stack)
            stack.push(node.val)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def __iter__(self):
        while not self.is_empty():
            yield self.pop()

bst = BinarySearchTree()
values_to_insert = [50, 30, 20, 40, 70, 60, 80]

for value in values_to_insert:
    bst.insert(value)

pre_order_stack = Stack()
in_order_stack = Stack()
post_order_stack = Stack()


bst.pre_order_traversal(bst.root, pre_order_stack)
bst.in_order_traversal(bst.root, in_order_stack)
bst.post_order_traversal(bst.root, post_order_stack)

print("Pre-order traversal from stack:", list(pre_order_stack))
print("In-order traversal from stack:", list(in_order_stack))
print("Post-order traversal from stack:", list(post_order_stack))
