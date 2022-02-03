from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon('Laser Gun', 2)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon
        print(f"{self.name} dealt {self.weapon.attack_power} damage to {dinosaur.name}.")