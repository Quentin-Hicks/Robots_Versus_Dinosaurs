from fleet import Fleet
from herd import Herd
import random

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        # only call display_welcome, battle, and display_winner here
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        # create a welcome to the thunderdome message
        print("-----WELCOME TO THE THUNDERDOME-----")

    def battle(self): # while the list length of robot and dino is greater than 0: loop through a dino and robot turn. call robo_turn and dino_turn here after successful testing
        while len(self.fleet.list) > 0 and len(self.herd.list) > 0:

            self.robo_turn()
            self.dino_turn()
        
        if len(self.fleet.list) == 0:
            print('All robots have 0 HP.')
        else:
            print('All dinosaurs have 0 HP.')

    def dino_turn(self): # using random but need to rememeber to use really good print statments to explain to the user what is happening in the dino turn.
        
        print('*' * 35)

        print("Choose a dinosaur to attack with")
        self.show_dino_attack_options()
        dino_user_choice = int(input())

        # print('*' * 35)

        # print("Who do you want to attack")
        # self.show_robo_attack_options()
        robo_opponent = random.randint(0, len(self.fleet.list) - 1 )# int(input())

        print('*' * 35)        

        self.herd.list[dino_user_choice].attack(self.fleet.list[robo_opponent])

        if self.fleet.list[robo_opponent].health <= 0:
            print(f"{self.fleet.list[robo_opponent].name} is defeated and can no longer battle.")
            self.fleet.list.remove(self.fleet.list[robo_opponent])

    def robo_turn(self):

        print('*' * 35)

        print("Choose a robot to attack with")
        self.show_robo_attack_options()
        robot_user_choice = int(input())

        # print('*' * 35)

        # print("Who do you want to attack")
        # self.show_dino_attack_options()
        dino_opponent = random.randint(0, len(self.herd.list) - 1 ) #int(input())

        print('*' * 35)

        self.fleet.list[robot_user_choice].attack(self.herd.list[dino_opponent])

        if self.herd.list[dino_opponent].health <= 0:
            print(f"{self.herd.list[dino_opponent].name} is defeated and can no longer battle.")
            self.herd.list.remove(self.herd.list[dino_opponent])

    def show_dino_attack_options(self):
        index = 0
        for dinosaur in self.herd.list:
            print(f'Press {index} to select {dinosaur.name} ({dinosaur.health} HP, {dinosaur.attack_power} Str, {dinosaur.energy} Energy).')
            index += 1

    def show_robo_attack_options(self):
        index = 0
        for robot in self.fleet.list:
            print(f'Press {index} to select {robot.name} ({robot.health} HP, {robot.battle_weapon.name}).')
            index += 1

    def display_winners(self):
        # if condition to check which team's list is greater than zero
        print('*' * 35)

        if len(self.fleet.list) > 0:
            print('Robots Win')
        else:
            print('Dinosaurs Win')