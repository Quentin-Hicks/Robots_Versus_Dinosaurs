from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.list = []

    def create_herd(self):
        dino_one = Dinosaur('Ripper', 2)
        dino_two = Dinosaur('Rexalator', 2)
        dino_three = Dinosaur('Rocky', 2)

        self.list.append(dino_one)
        self.list.append(dino_two)
        self.list.append(dino_three)