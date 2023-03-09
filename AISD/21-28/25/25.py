class Transport:
    def __init__(self, brand, coordinates):
        self.brand = brand
        self.coordinates = coordinates

    def __str__(self):
        return f"{self.brand}, coordinates: {self.coordinates}"

    def is_in_coordinates(self, min_coords, max_coords):
        return min_coords[0] <= self.coordinates[0] <= max_coords[0] and min_coords[1] <= self.coordinates[1] <= max_coords[1]

class Airplane(Transport):
    def __init__(self, brand, max_speed, max_height, passenger_count, coordinates):
        super().__init__(brand, coordinates)
        self.max_speed = max_speed
        self.max_height = max_height
        self.passenger_count = passenger_count

    def __str__(self):
        return super().__str__() + f", max speed: {self.max_speed}, max height: {self.max_height}, passenger count: {self.passenger_count}"

class Car(Transport):
    def __init__(self, brand, number, year, coordinates):
        super().__init__(brand, coordinates)
        self.number = number
        self.year = year

    def __str__(self):
        return super().__str__() + f", number: {self.number}, year: {self.year}"

class Ship(Transport):
    def __init__(self, name, speed, passenger_count, home_port, coordinates):
        super().__init__(name, coordinates)
        self.speed = speed
        self.passenger_count = passenger_count
        self.home_port = home_port

    def __str__(self):
        return super().__str__() + f", speed: {self.speed}, passenger count: {self.passenger_count}, home port: {self.home_port}"

# Пример использования
n = 4

transport_list = [
    Airplane("Boeing 747", 900, 12000, 400, (55.75, 37.62)),
    Car("Honda Pilot ", "Е811КК197", 2009, (55.75, 37.62)),
    Ship("Queen Mary 2", 30, 2500, "Southampton", (50.9, -1.4)),
    Airplane("Airbus A320", 840, 11000, 200, (55.41, 37.9))
]

# Вывод информации о транспортных средствах
for transport in transport_list:
    print(transport)

# Поиск транспортных средств в заданных координатах
min_coords = (55.4, 37.6)
max_coords = (55.8, 38.0)

transport_in_coordinates = [t for t in transport_list if t.is_in_coordinates(min_coords, max_coords)]

# Вывод найденных транспортных средств
print(f"Transport within coordinates {min_coords}-{max_coords}:")
for transport in transport_in_coordinates:
    print(transport)
