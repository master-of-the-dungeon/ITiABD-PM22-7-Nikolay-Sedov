from collections import deque

class Car:
    def __init__(self, car_id):
        self.car_id = car_id

class CarWash:
    def __init__(self):
        self.stages = {
            'мойки': 5,
            'воска': 3,
            'сушки': 2
        }
        self.total_time = 0
        self.queue = deque()

    def add_car(self, car):
        self.queue.append(car)

    def process(self):
        while self.queue:
            car = self.queue.popleft()
            car_time = 0
            print(f'Машина {car.car_id} в обслуживании:')
            for stage, time in self.stages.items():
                car_time += time
                print(f' Стадия {stage}: {time} минут')
            self.total_time += car_time
            print(f'  Всего машину мыли {car.car_id}: {car_time} минут\n')

    def get_total_time(self):
        return self.total_time

# Пример использования
car_wash = CarWash()
car_wash.add_car(Car(1))
car_wash.add_car(Car(2))
car_wash.add_car(Car(3))

car_wash.process()
print(f'Суммарно затрачено: {car_wash.get_total_time()} минут')
