from fleet import Fleet
from herd import Herd
import random

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        # only call display, battle, and display winner methods here
        # self.battle()
        pass
        self.robo_turn()
        self.dino_turn()

    def display_welcome(self):
        # create a welcome to the thunderdome message
        print("-----WELCOME TO THE THUNDERDOME-----")
        print('*' * 35)

    def battle(self): # while the list length of robot and dino is greater than 0: loop through a dino and robot turn. call robo_turn and dino_turn here after successful testing
        while len(self.fleet.list) - 1 > 0 or len(self.herd.list) - 1 > 0:
            self.robo_turn() # move to battle
            self.dino_turn() # move to battle
        # self.display_winners()

    def dino_turn(self): # using random but need to rememeber to use really good print statments to explain to the user what is happening in the dino turn.
        print('*' * 35)

        print("Choose a dinosaur to attack with")
        self.show_dino_attack_options()
        dino_user_choice = int(input())

        print("Who do you want to attack")
        self.show_robo_attack_options()
        robo_opponent = int(input())
        print('*' * 35)

        self.herd.list[dino_user_choice].attack(self.fleet.list[robo_opponent])

        if self.fleet.list[robo_opponent].health <= 0:
            self.fleet.list.remove(self.fleet.list[robo_opponent])

    def robo_turn(self):
        print('*' * 35)

        print("Choose a robot to attack with")
        self.show_robo_attack_options()
        robot_user_choice = int(input())

        print("Who do you want to attack")
        self.show_dino_attack_options()
        dino_opponent = int(input())
        print('*' * 35)

        self.fleet.list[robot_user_choice].attack(self.herd.list[dino_opponent])

        if self.herd.list[dino_opponent].health <= 0:
            self.herd.list.remove(self.herd.list[dino_opponent])

    def show_dino_attack_options(self):
        index = 0
        for dinosaur in self.herd.list:
            print(f'Press {index} to select {dinosaur.name} ({dinosaur.health} HP).')
            index += 1

    def show_robo_attack_options(self):
        index = 0
        for robot in self.fleet.list:
            print(f'Press {index} to select {robot.name} ({robot.health} HP).')
            index += 1

    def display_winners(self):
        pass # if condition to check which team's list is greater than zero