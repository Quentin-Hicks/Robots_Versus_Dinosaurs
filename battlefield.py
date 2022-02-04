from fleet import Fleet
from herd import Herd
import random

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        # only call display, battle, and display winner methods here
        self.robo_turn() # move to battle
        self.dino_turn() # move to battle

    def display_welcome(self):
        # create a welcome to the thunderdome message
        print("WELCOME TO THE THUNDERDOME!!!")
        print('*' * 10)

    def battle(self): # while the list length of robot and dino is greater than 0: loop through a dino and robot turn. call robo_turn and dino_turn here after successful testing
        pass

    def dino_turn(self): # using random but need to rememeber to use really good print statments to explain to the user what is happening in the dino turn.
        print("Choose a dinosaur to attack with")
        self.show_dino_attack_options()
        dino_user_choice = int(input())

        self.herd.list[dino_user_choice].attack(self.fleet.list[0])

    def robo_turn(self):
        print("Choose a robot to attack with")
        self.show_robo_attack_options()
        robot_user_choice = int(input())

        self.fleet.list[robot_user_choice].attack(self.herd.list[0])

    def show_dino_attack_options(self):
        index = 0
        for dinosaur in self.herd.list:
            print(f'Press {index} to select {dinosaur.name}.')
            index += 1

    def show_robo_attack_options(self):
        index = 0
        for robot in self.fleet.list:
            print(f'Press {index} to select {robot.name}.')
            index += 1

    def display_winners(self):
        pass

# fleet_one = Fleet() # move to battle method
# herd_one = Herd() # move to battle method

# fleet_one.create_fleet()
# herd_one.create_herd()

# fleet_one.list[random.randint(0, len(fleet_one.list) -1)].attack(herd_one.list[random.randint(0, len(herd_one.list) -1)])
# fleet_one.list[1].attack(herd_one.list[0])
# fleet_one.list[1].attack(herd_one.list[0])