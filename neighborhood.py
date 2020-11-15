from random import randint
from NPC import NPC

class House():
    def __init__(self):
        self.isSafe = False
        self.population = randint(0,10)
        self.numMonsters = self.population
        self.createHouse()

    def createHouse(self):
        arrNPCs = [NPC() for i in range(self.population)]
        print("Creating a house with", len(arrNPCs), "monsters.")

class Neighborhood():
    def __init__(self, size):
        self.numHouses = size
        self.createNeighborhood()

    def createNeighborhood(self):
        print("Creating a neighborhood with", 9 , "houses.")
        neighborhood = [[House() for j in range(self.numHouses)] for i in range(self.numHouses)]
