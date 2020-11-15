from random import randint

class NPC():
    def __init__(self):
        self.createNPC()

    def createNPC(self):
        print("Created a Monster")
        choice = randint(1, 4)
        switcher = {
            1: Zombie(),
            2: Vampire(),
            3: Ghoul(),
            4: Werewolf()
        }
        return switcher.get(choice, Zombie())

class Zombie(NPC):
    def __init__(self):
        self.hitPoints = randint(50, 100)
        self.attackStr = randint(0, 10)
        self.description = "a Zombie, which is weak to SourStraws. It does", self.attackStr, "damage."

    def isHarmed(self):
        print("Check if harmed")

    def attack(self):
        print("Deal damage")

class Vampire(NPC):
    def __init__(self):
        self.hitPoints = randint(100, 200)
        self.attackStr = randint(10, 20)
        self.description = "a Vampire, which is immune to ChocolateBars."

    def isHarmed(self):
        print("Check if harmed")

    def attack(self):
        print("Deal damage")

class Ghoul(NPC):
    def __init__(self):
        self.hitPoints = randint(40, 80)
        self.attackStr = randint(15, 30)
        self.description = "a Ghoul, which is very weak to NerdBombs."

    def isHarmed(self):
        print("Check if harmed")

    def attack(self):
        print("Deal damage")

class Werewolf(NPC):
    def __init__(self):
        self.hitPoints = 200
        self.attackStr = randint(0, 40)
        self.description = "a Werewolf, which is immune to both ChocolateBars and SourStraws."

    def isHarmed(self):
        print("Check if harmed")

    def attack(self):
        print("Deal damage")