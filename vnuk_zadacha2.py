from collections import deque

class Customer:
    def __init__(self, name, items):
        self.name = name
        self.items = items

class Checkout:
    def __init__(self, checkout_id):
        self.checkout_id = checkout_id
        self.queue = deque()
        self.total_time = 0

    def add_customer(self, customer):
        self.queue.append(customer)

    def process(self):
        while self.queue:
            customer = self.queue.popleft()
            time_to_process = customer.items * 1  
            print(f'Касса {self.checkout_id} обслуживает {customer.name}, {customer.items} товаров, время обработки {time_to_process} минут.')
            self.total_time += time_to_process

    def get_total_time(self):
        return self.total_time

class Supermarket:
    def __init__(self, num_checkouts):
        self.checkouts = [Checkout(i+1) for i in range(num_checkouts)]

    def add_customer_to_shortest_queue(self, customer):
        shortest_queue = min(self.checkouts, key=lambda c: len(c.queue))
        shortest_queue.add_customer(customer)

    def process_all_checkouts(self):
        for checkout in self.checkouts:
            checkout.process()

    def get_total_time(self):
        return sum(checkout.get_total_time() for checkout in self.checkouts)


supermarket = Supermarket(3)  
supermarket.add_customer_to_shortest_queue(Customer("Лёха", 5))
supermarket.add_customer_to_shortest_queue(Customer("Костя", 7))
supermarket.add_customer_to_shortest_queue(Customer("Ваня", 4))
supermarket.add_customer_to_shortest_queue(Customer("Игорь", 10))
supermarket.add_customer_to_shortest_queue(Customer("Вазген", 3))

supermarket.process_all_checkouts()
print(f'Общее время для всех касс: {supermarket.get_total_time()} минут')
