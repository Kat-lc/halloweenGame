from random import randint, uniform

class Weapon():
    def __init__(self):
        self.name = "Weapon"
        self.attackMod = 1
        self.ammo = 1

    def getWeapon(self):
        return self.name

    def getAmmo(self):
        return self.ammo

class HersheyKiss(Weapon):
    def __init__(self):
        self.name = "HersheyKiss"
        self.attackMod = 1
        self.description = "a HersheyKiss, a weak weapon with unlimited ammo."

    def use(self):
        print("Use")

    def getWeapon(self):
        return self.name

    def getAmmo(self):
        return "unlimited"

    def getAttack(self):
        return self.attackMod

class SourStraw(Weapon):
    def __init__(self):
        self.name = "SourStraw"
        self.ammo = 2
        self.attackMod = uniform(1.0, 1.75)
        self.outOfAmmo = False
        self.description = ""

    def getWeapon(self):
        return self.name

    def getAmmo(self):
        return self.ammo

    def getAttack(self):
        return self.attackMod

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

    def getAmmo(self):
        return self.ammo

    def getAttack(self):
        return self.attackMod

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

    def getAmmo(self):
        return self.ammo

    def getAttack(self):
        return self.attackMod

    def use(self):
        print("Reducing ammo")
        print("Check if out of ammo")