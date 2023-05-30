class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            i = 0
            while i < index-1 and current.next:
                current = current.next
                i += 1
            new_node.next = current.next
            current.next = new_node

    def delete(self, index):
        if not self.head:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            i = 0
            while i < index-1 and current.next:
                current = current.next
                i += 1
            if not current.next:
                return
            current.next = current.next.next

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.value) + " "
            current = current.next
        return result

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
print(linked_list) # 1 2 4
linked_list.insert(3, 2)
print(linked_list) # 1 2 3 4
