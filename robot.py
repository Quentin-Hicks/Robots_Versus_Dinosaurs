from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon_list = []
        self.weapons()
        self.weapon_choice()
        self.battle_weapon
        #self.weapon = Weapon('Laser Gun', 3)

    def attack(self, dinosaur):
        dinosaur.health -= self.battle_weapon.attack_power

        print(f"{self.name} dealt {self.battle_weapon.attack_power} damage to {dinosaur.name} with {self.battle_weapon.name}.")
        
        # print(f"{dinosaur.name} has {dinosaur.health} health points left.")

    def weapons(self):

        weapon_one = Weapon('Cannon', 3)
        weapon_two = Weapon('Gun', 2)
        weapon_three = Weapon('Sword', 1)

        self.weapon_list.append(weapon_one)
        self.weapon_list.append(weapon_two)
        self.weapon_list.append(weapon_three)
    
    def weapon_choice(self):

        print(f'Choose a weapon for {self.name}: ')

        index = 0
        for weapon in self.weapon_list:
            print(f'Press {index} to select {weapon.name}')
            index += 1

        user_weapon_choice = int(input())
        self.battle_weapon = self.weapon_list[user_weapon_choice]
