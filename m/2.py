class ChainElement:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_chain(length):
    if length <= 0:
        return None

    first_element = ChainElement(0)
    current_element = first_element

    for i in range(1, length):
        new_element = ChainElement(i)
        current_element.next = new_element
        current_element = new_element

    return first_element

# Пример использования функции create_chain
chain_length = 5
chain = create_chain(chain_length)

if chain is None:
    print("Цепочка не создана")
else:
    current_element = chain
    while current_element is not None:
        print(current_element.value)
        current_element = current_element.next
