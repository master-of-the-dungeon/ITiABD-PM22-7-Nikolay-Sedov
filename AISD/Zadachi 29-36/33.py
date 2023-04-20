class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def remove_large_elements(head, max_value):
    if head is None:
        return None

    current_node = head
    while True:
        if current_node.value > max_value:
            if current_node == head:
                head = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        current_node = current_node.next
        if current_node == head:
            break

    return head


head = Node(1)
head.prev = Node(8)
head.prev.next = head
head.next = Node(5)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next
head.next.next.next = Node(7)
head.next.next.next.prev = head.next.next
head.next.next.next.next = head
head.prev.next = head


print("Original List:")
current_node = head
while True:
    print(current_node.value, end=' ')
    current_node = current_node.next
    if current_node == head:
        break


head = remove_large_elements(head, 5)


print("\nModified List:")
current_node = head
while True:
    print(current_node.value, end=' ')
    current_node = current_node.next
    if current_node == head:
        break
