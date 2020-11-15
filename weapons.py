from random import randint, uniform

class Weapon():
    def __init__(self):
        self.createWeapon()
        self.name = "Weapon"

    def createWeapon(self):
        print("Created a weapon")
        choice = randint(1, 4)
        switcher = {
            1: HersheyKiss(),
            2: SourStraw(),
            3: ChocolateBar(),
            4: NerdBomb()
        }
        return switcher.get(choice, HersheyKiss())

    def getWeapon(self):
        return self.name


class HersheyKiss(Weapon):
    def __init__(self):
        self.name = "HersheyKiss"
        self.attackMod = 1
        self.description = "a HersheyKiss, a weak weapon with unlimited ammo."

    def use(self):
        print("Use")

    def getWeapon(self):
        return self.name

class SourStraw(Weapon):
    def __init__(self):
        self.name = "SourStraw"
        self.ammo = 2
        self.attackMod = uniform(1.0, 1.75)
        self.outOfAmmo = False
        self.description = ""

    def getWeapon(self):
        return self.name

    def use(self):
        print("Reducing ammo")
        print("Check if out of ammo")

class ChocolateBar(Weapon):
    def __init__(self):
        self.name = "ChocolateBar"
        self.ammo = 4
        self.attackMod = uniform(2.0, 2.4)
        self.outOfAmmo = False
        self.description = ""

    def getWeapon(self):
        return self.name

    def use(self):
        print("Reducing ammo")
        print("Check if out of ammo")

class NerdBomb(Weapon):
    def __init__(self):
        self.name ="NerdBomb"
        self.ammo = 1
        self.attackMod = uniform(3.5, 5)
        self.outOfAmmo = False
        self.description = ""

    def getWeapon(self):
        return self.name

    def use(self):
        print("Reducing ammo")
        print("Check if out of ammo")