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

    def remove_duplicates(self):
        unique_items = []
        while not self.is_empty():
            item = self.pop()
            if item not in unique_items:
                unique_items.append(item)
        for item in reversed(unique_items):
            self.push(item)

    def __str__(self):
        current_node = self.top
        stack_str = ""
        while current_node is not None:
            stack_str += str(current_node.value) + " "
            current_node = current_node.next
        return stack_str

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.stack2.is_empty():
            while not self.stack1.is_empty():
                item = self.stack1.pop()
                self.stack2.push(item)
        return self.stack2.pop()

    def remove_duplicates(self):
        self.stack1.remove_duplicates()
        self.stack2.remove_duplicates()

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return str(self.stack2) + " " + str(self.stack1)[::-1]

# Пример использования
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(4)
my_queue.enqueue(5)
print("Очередь до удаления повторяющихся элементов:", my_queue)
my_queue.remove_duplicates()
print("Очередь после удаления повторяющихся элементов:", my_queue)
