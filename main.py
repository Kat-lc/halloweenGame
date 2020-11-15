from neighborhood import Neighborhood
from player import Player

options = ["1", "2", "3", "4", "5", "6", "7"]
displayOptions = ["1: Display Options", "2: Investigate", "3: Move", "4: Attack", "5: Display Inventory", "6: Forfeit Game"]
directions = ["1", "2", "3", "4", "5"]
displayDirections = ["1: Display Directions", "2: North", "3: East", "4: South", "5: West"]
inventory = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

result = "lost"
gameActivity = True

class Game:
    def __init__(self):
        print("Welcome to the Halloween Python Game!")
        self.myNeighborhood = Neighborhood(1)
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
                self.myPlayer.investigate()
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
                    self.myPlayer.attack(weapon) #String to int here if possible, use index
            elif input == '5':
                self.myPlayer.displayInv()
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

    def exit(self):
        print("Game over! You", result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainGame = Game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
