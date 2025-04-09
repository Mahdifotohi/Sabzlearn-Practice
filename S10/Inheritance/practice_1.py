class Animal:
    def __init__(self, name:str, species:str):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound.")


class Mammal(Animal):
    def __init__(self, name, species, legs:int):
        self.legs = legs
        super().__init__(name, species)

    def make_sound(self):
        print("Generic mammal sound.")

class Dog(Mammal):
    def __init__(self, name, species, legs, race:str):
        self.race = race
        super().__init__(name, species, legs)

    def make_sound(self):
        print("Woof!")




dog = Dog("Buddy", "Canine", 4, "Golden Retriever")
dog.make_sound()     # Output: Woof!