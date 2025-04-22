class Vehicle():
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def move(self):
        return "The vehicle is moveing."

class Car(Vehicle):
    def __init__(self, color, weight, speed):
        super().__init__(color, weight)
        self.speed = speed

    def move(self):
        return f" The car is driving at {self.speed} km/h. "


class Bicycle(Vehicle):
    def __init__(self, color, weight, gear_count):
        super().__init__(color, weight)
        self.gear_count = gear_count

    def mive(self):
        return f"The bicycle is pedaling with {self.gear_count} gears."


class Airplane(Vehicle):
    def __init__(self, color, weight, altitude):
        super().__init__(color, weight)
        self.altitude = altitude

    def move(self):
        return f"The airplane is flying at an altitude of {self.altitude} meters."


class Lamborghini(Car):
    def __init__(self, color, weight, speed, model):
        super().__init__(color, weight, speed)
        self.model = model

    def move(self):
        return f"The Lamborghini {self.model} is racing at {self.speed} km/h."


class Benz(Car):
    def __init__(self, color, weight, speed, model):
        super().__init__(color, weight, speed)
        self.model = model

    def move(self):
        return f"The Benz {self.model} is cruising at {self.speed} km/h."
    

# Example usage
vehicles = [
    Vehicle("White", 1500),
    Car("Red", 1200, 180),
    Bicycle("Blue", 15, 21),
    Airplane("Silver", 8000, 10000),
    Lamborghini("Yellow", 1400, 350, "Aventador"),
    Benz("Black", 1600, 240, "S-Class")
]

for v in vehicles:
    print(v.move())
