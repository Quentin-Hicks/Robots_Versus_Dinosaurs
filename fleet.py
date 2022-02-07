from robot import Robot

class Fleet:

    def __init__(self):
        self.list = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot('Megas')
        robot_two = Robot('Raging Bender')
        robot_three = Robot('Big O')

        self.list.append(robot_one)
        self.list.append(robot_two)
        self.list.append(robot_three)