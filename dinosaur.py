
class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 10
        self.energy = 10

    def attack(self, robot): # robot.health - self.attack_power and use print to fill in the user as to what happend
        robot.health -= self.attack_power

        print(f"{self.name} dealt {self.attack_power} damage to {robot.name}.")

        self.energy -= 2

        