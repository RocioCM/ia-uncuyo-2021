from random import randrange
import math


class Environment:
    obstaclesRate = 0.3
    size = 10

    def __init__(self):
        self.matrix = [[u"\u2B1C" for i in range(
            self.size)] for j in range(self.size)]  # All white
        self.__createObstacles()

    def __createObstacles(self):
        obstaclesLeft = math.ceil(
            self.obstaclesRate * self.size ** 2)
        while (obstaclesLeft > 0):
            row = randrange(self.size)
            column = randrange(self.size)
            alreadyHasObstacle = self.hasObstacle(row, column)
            if (not(alreadyHasObstacle)):
                self.matrix[row][column] = u"\u2B1B"  # Black
                obstaclesLeft -= 1

    def hasObstacle(self, row, column):
        return self.matrix[row][column] == u"\u2B1B"  # Black

    def printEnvironment(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.matrix[i][j], end='')
            print('')
        print('')
