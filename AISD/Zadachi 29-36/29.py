class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            popped_node = self.top
            self.top = popped_node.next
            popped_node.next = None
            return popped_node.value

    def remove_negative(self):
        current_node = self.top
        previous_node = None
        while current_node is not None:
            if current_node.value < 0:
                if previous_node is None:
                    self.top = current_node.next
                else:
                    previous_node.next = current_node.next
            else:
                previous_node = current_node
            current_node = current_node.next

    def __str__(self):
        current_node = self.top
        stack_str = ""
        while current_node is not None:
            stack_str += str(current_node.value) + " "
            current_node = current_node.next
        return stack_str

# Пример использования
my_stack = Stack()
my_stack.push(5)
my_stack.push(-2)
my_stack.push(7)
my_stack.push(-1)
print("Стек до удаления отрицательных элементов:", my_stack)
my_stack.remove_negative()
print("Стек после удаления отрицательных элементов:", my_stack)
