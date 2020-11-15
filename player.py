from random import randint
from weapons import Weapon


class Player:
    print("Creating player...")
    def __init__(self):
        self.hitpoints = randint(100, 125)
        self.attackVal = randint(10, 20)
        self.inventory = [Weapon() for i in range(10)]

    def investigate(self):
        print("Investigating")

    def status(self):
        print("Checking status")

    def interact(self, typeNPC):
        print("Interacting with")

    def attack(self, weaponType):
        print("Attacking")

    def heal(self):
        print("Healing")

    def move(self, direction):
        print("Moving in", direction)

    def displayInv(self):
        for i in self.inventory:
            print(i, ":", i.getWeapon(), "\n")