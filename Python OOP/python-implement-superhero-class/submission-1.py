class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health

bat_man = SuperHero ("Batman", "Intelligence", 100)
print(f"{bat_man.name}\n{bat_man.power}\n{bat_man.health}")

super_man = SuperHero ("Superman", "Strength", 150)
print(f"{super_man.name}\n{super_man.power}\n{super_man.health}")
