from collections import deque

class Visitor:
    def __init__(self, name, ride_time):
        self.name = name
        self.ride_time = ride_time

class AmusementRide:
    def __init__(self):
        self.queue = deque()
        self.total_time = 0

    def add_visitor(self, visitor):
        self.queue.append(visitor)

    def process(self):
        while self.queue:
            visitor = self.queue.popleft()
            print(f'{visitor.name} катается {visitor.ride_time} минут.')
            self.total_time += visitor.ride_time

    def get_total_time(self):
        return self.total_time


ride = AmusementRide()
ride.add_visitor(Visitor("Максим", 5))
ride.add_visitor(Visitor("Коля", 7))
ride.add_visitor(Visitor("Тимур", 4))

ride.process()
print(f'Общее время для всех посетителей: {ride.get_total_time()} минут')
