class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")


# TODO: Create the Dog and Cat classes with make_sound method
class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")

def display_Animal(anml: Animal):
    anml.make_sound()


# Do not change the code below
animal = Animal("Rabbit")
display_Animal(animal)

animal = Dog("Buddy")
display_Animal(animal)

animal = Cat("Whiskers")
display_Animal(animal)
