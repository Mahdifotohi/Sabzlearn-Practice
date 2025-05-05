from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        """This method must be written."""

    @abstractmethod
    def stop(self):
        """This method must be written."""


class SportsCar(Car):
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} SportsCar is starts incredibly fast.")

    def stop(self):
        print(f"{self.brand} SportsCar is stopping gracefully.")

class Sedan(Car):
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} Sedan is starting smoothly.")

    def stop(self):
        print(f"{self.brand} Sedan is stopping safely.")


# Example usage
if __name__ == "__main__":
    sports_car = SportsCar("Ferrari")
    sedan = Sedan("Toyota")

    sports_car.start()
    sports_car.stop()

    sedan.start()
    sedan.stop()
        