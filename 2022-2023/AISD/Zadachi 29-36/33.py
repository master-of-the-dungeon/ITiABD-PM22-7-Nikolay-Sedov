class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def delete_greater_than_value(head: Node, val: int) -> Node:
    # Если список пуст, возвращаем None
    if not head:
        return None

    # Находим первый элемент, который не больше заданного значения
    current = head
    while current.val > val:
        current = current.next
        if current == head:
            return head
    head = current

    # Проходим по списку и удаляем элементы, которые больше заданного значения
    current = head.next
    while current != head:
        if current.val > val:
            # Обновляем ссылки на следующий и предыдущий узлы, чтобы исключить элемент из списка
            current.prev.next = current.next
            current.next.prev = current.prev
            current = current.next
            continue
        current = current.next

    return head

# Создаем кольцевой двусвязный список
head = Node(1)
head.next = Node(3)
head.next.prev = head
head.next.next = Node(5)
head.next.next.prev = head.next
head.next.next.next = Node(7)
head.next.next.next.prev = head.next.next
head.next.next.next.next = head
head.prev = head.next.next.next

# Удаляем элементы, которые больше 4
head = delete_greater_than_value(head, 4)

# Выводим список
current = head
while True:
    print(current.val, end=' ')
    current = current.next
    if current == head:
        break
