class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def sum_lists(list1, list2):
    result = None
    current1 = list1
    current2 = list2
    carry = 0
    while current1 is not None or current2 is not None or carry > 0:
        sum = carry
        if current1 is not None:
            sum += current1.value
            current1 = current1.next
        if current2 is not None:
            sum += current2.value
            current2 = current2.next
        digit = sum % 10
        carry = sum // 10
        new_node = Node(digit)
        if result is None:
            result = new_node
        else:
            new_node.next = result
            result.prev = new_node
            result = new_node
    return result



list1 = Node(5)
list1.prev = None
list1.next = Node(4)
list1.next.prev = list1
list1.next.next = Node(3)
list1.next.next.prev = list1.next


list2 = Node(7)
list2.prev = None
list2.next = Node(8)
list2.next.prev = list2
list2.next.next = Node(9)
list2.next.next.prev = list2.next

result = sum_lists(list1, list2)


while result is not None:
    print(result.value, end='')
    result = result.next
