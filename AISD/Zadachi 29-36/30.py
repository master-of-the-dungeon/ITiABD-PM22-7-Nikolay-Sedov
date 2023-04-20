class UniqueQueue:
    def __init__(self):
        self.queue = []

    def add_element(self, element):
        self.queue.append(element)

    def remove_duplicates(self):
        unique_queue = []
        for element in self.queue:
            if element not in unique_queue:
                unique_queue.append(element)
        self.queue = unique_queue

queue = UniqueQueue()
queue.add_element(1)
queue.add_element(2)
queue.add_element(3)
queue.add_element(2)
queue.add_element(4)
queue.remove_duplicates()
print(queue.queue)
