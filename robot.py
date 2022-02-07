from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapon_list = []
        self.weapons()
        self.weapon_choice()
        self.battle_weapon
        self.power_level = 50

    def attack(self, dinosaur):
        dinosaur.health -= self.battle_weapon.attack_power

        print(f"{self.name} dealt {self.battle_weapon.attack_power} damage to {dinosaur.name} with {self.battle_weapon.name}.")

        self.power_level -= 10

    def weapons(self):

        weapon_one = Weapon('Laser Cannon', 12)
        weapon_two = Weapon('Particle Gun', 12)
        weapon_three = Weapon('Saber Sword', 12)

        self.weapon_list.append(weapon_one)
        self.weapon_list.append(weapon_two)
        self.weapon_list.append(weapon_three)
    
    def weapon_choice(self):

        print(f'Choose a weapon for {self.name}: ')

        index = 0
        for weapon in self.weapon_list:
            print(f'Press {index} to select {weapon.name} (Atk Pwr: {weapon.attack_power})')
            index += 1

        user_weapon_choice = int(input())
        self.battle_weapon = self.weapon_list[user_weapon_choice]
