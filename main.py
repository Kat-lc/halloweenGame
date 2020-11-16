from random import randint

from NPC import NPC
from weapons import HersheyKiss, SourStraw, ChocolateBar, NerdBomb

options = ["1", "2", "3", "4", "5", "6", "7"]
displayOptions = ["1: Display Options", "2: Enter/Exit House", "3: Move", "4: Attack", "5: Status", "6: Forfeit Game"]
directions = ["1", "2", "3", "4", "5"]
displayDirections = ["1: Display Directions", "2: North", "3: East", "4: South", "5: West"]
inventory = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

result = "lost"
gameActivity = True
size = 1


class Game:
    x = 0
    y = 0

    def __init__(self):
        print("Welcome to the Halloween Python Game!")
        self.myNeighborhood = Neighborhood(size)
        self.neighborhood = self.myNeighborhood.getNeighborhood()
        self.myPlayer = Player()
        self.activeGame()

    def display(self, input: list):
        for i in input:
            print(i)

    def activeGame(self):
        print("Running the game")
        while gameActivity is True:
            print("What would you like to do? Press 1 for options.")
            input = self.getInput(options)
            if input == '1':
                self.display(displayOptions)
            elif input == '2':
                self.myPlayer.interact()
            elif input == '3':
                while True:
                    print("Which direction would you like to move? Press 1 for options.")
                    direction = self.getInput(directions)
                    if direction == '1':
                        self.display(displayDirections)
                    else:
                        self.myPlayer.move(direction)
                        break
            elif input == '4':
                print("Which weapon would you like to use? Press 1 for options.")
                weapon = self.getInput(inventory)
                if weapon == '1':
                    self.myPlayer.displayInv()
                else:
                    self.myPlayer.attack(weapon)  # String to int here if possible, use index
            elif input == '5':
                self.myPlayer.status()
            elif input == '6':
                self.exit()

    def getInput(self, validInput: list):
        while True:
            userInput = input()

            if userInput not in validInput:
                print("Oops! Invalid input. Please us one of the following:\n")
                print(validInput)
                userInput = None
            else:
                return userInput

    def getPosition(self, x, y):
        return self.neighborhood[x][y]

    def exit(self):
        print("Game over! You", result)


class Neighborhood(Game):
    totalMonsters = 0

    def __init__(self, size):
        self.numHouses = (size + 1) ** 2
        print(self.numHouses)
        self.neighborhood = [[House() for j in range(size + 1)] for i in range(size + 1)]
        self.totalMonsters = 0
        print("There is a total of", Neighborhood.totalMonsters, "monsters spread across", self.numHouses, "houses in a squared grid")

    def getNeighborhood(self):
        return self.neighborhood

class House(Neighborhood):
    def __init__(self):
        self.isSafe = False
        self.population = randint(0, 10)
        Neighborhood.totalMonsters += self.population
        self.createHouse()

    def createHouse(self):
        arrNPCs = [NPC() for i in range(self.population)]
        print("Creating a house with", len(arrNPCs), "monsters.")


class Player(Game):
    print("Creating player...")

    def __init__(self):
        self.hitpoints = randint(100, 125)
        self.attackVal = randint(10, 20)
        self.inHouse = False
        self.inventory = [self.createWeapon() for i in range(10)]

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

    def interact(self):
        print(self.inHouse)
        if self.inHouse is False:
            self.inHouse = True
            print("Entering house. Prepare to fight!")
            print("There are a total of")
        else:
            self.inHouse = False
            print("Exiting house. Time to rest!")

    def move(self, direction):
        if self.inHouse is False:
            if direction == '2':
                if 0 < Game.x:
                    print("Moving ", end="", flush=True)
                    Game.x = Game.x - 1
                    print("North")
                    print("House: ", )
                else:
                    print("Can't go that direction!")
            if direction == '3':
                if Game.y < size:
                    print("Moving ", end="", flush=True)
                    Game.y = Game.y + 1
                    print("East")
                else:
                    print("Can't go that direction!")
            if direction == '4':
                if Game.x < size:
                    print("Moving ", end="", flush=True)
                    Game.x = Game.x + 1
                    print("South")
                else:
                    print("Can't go that direction!")
            if direction == '5':
                if 0 < Game.y:
                    print("Moving ", end="", flush=True)
                    Game.y = Game.y - 1
                    print("West")
                else:
                    print("Can't go that direction!")
        else:
            print("You must leave this house before traveling to a new one!")

    def attack(self, weaponType):
        print("Attacking")

    def takeDamage(self, damage):
        print("Took damage")

    def status(self):
        print("Health: ", self.hitpoints)
        print("Attack: ", self.attackVal)
        print("Inventory")
        print("------------------")
        self.displayInv()

    def displayInv(self):
        for i in self.inventory:
            print(i.getWeapon(), ":", "Ammo at", i.getAmmo(), "left")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainGame = Game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
