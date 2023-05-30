class Car:
    def __init__(self, make, model, year, color, speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_speed(self):
        return self.speed

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount

car = Car("Honda", "S2000", 2005, "British Racing Green", 160)

print("Make:", car.get_make())
print("Model:", car.get_model())
print("Year:", car.get_year())
print("Color:", car.get_color())
print("Speed:", car.get_speed())

car.accelerate(260)
print("Speed after acceleration:", car.get_speed())

car.brake(190)
print("Speed after braking:", car.get_speed())
