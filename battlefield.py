from fleet import Fleet
from herd import Herd
import random

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("-----WELCOME TO THE THUNDERDOME-----")

    def battle(self):
        while len(self.fleet.list) > 0 and len(self.herd.list) > 0:

            if len(self.fleet.list) > 0:
                self.robo_turn()
            else:
                print('All robots have 0 HP.')

            if len(self.herd.list) > 0:
                self.dino_turn()
            else:
                print('All dinosaurs have 0 HP left.')

    def dino_turn(self):
        print('*' * 35)

        print("Choose a dinosaur to attack with")
        self.show_dino_attack_options()
        dino_user_choice = int(input())

        print('*' * 35)

        print("Who do you want to attack")
        self.show_robo_attack_options()
        robo_opponent = int(input())

        print('*' * 35)        

        if self.herd.list[dino_user_choice].energy > 0:
            self.herd.list[dino_user_choice].attack(self.fleet.list[robo_opponent])
        else:
            print(f"{self.herd.list[dino_user_choice].name} has no energy and cannot attack.")

        if self.fleet.list[robo_opponent].health <= 0:
            print(f"{self.fleet.list[robo_opponent].name} is defeated and can no longer battle.")
            self.fleet.list.remove(self.fleet.list[robo_opponent])

    def robo_turn(self):
        print('*' * 35)

        print("Choose a robot to attack with")
        self.show_robo_attack_options()
        robot_user_choice = int(input())

        print('*' * 35)

        print("Who do you want to attack")
        self.show_dino_attack_options()
        dino_opponent = int(input())

        print('*' * 35)

        if self.fleet.list[robot_user_choice].power_level > 0:
            self.fleet.list[robot_user_choice].attack(self.herd.list[dino_opponent])
        else:
            print(f"{self.fleet.list[robot_user_choice].name} has no power and cannot attack.")

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
            print(f'Press {index} to select {robot.name} ({robot.health} HP, {robot.power_level} Power, {robot.battle_weapon.name}).')
            index += 1

    def display_winners(self):
        print('*' * 35)

        if len(self.fleet.list) > 0:
            print('Robots Win')
        else:
            print('Dinosaurs Win')