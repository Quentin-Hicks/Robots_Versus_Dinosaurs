from robot import Robot

class Fleet:

    def __init__(self):
        self.list = []

    def create_fleet(self): # on battlefield we need to instanciate our fleet then call create_fleet method to assemble our 3 robots, same for dino
        # robot_one = Robot("R2-D2") make 3 and append them to the list
        self.robot_one = Robot('Megas')
        self.robot_two = Robot('Raging Bender')
        self.robot_three = Robot('Big O')
        pass