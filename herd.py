from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.list = []

    def create_herd(self):
        self.dino_one = Dinosaur('Ripper', 2)
        self.dino_two = Dinosaur('Rexalator', 2)
        self.dino_three = Dinosaur('Rocky', 2)