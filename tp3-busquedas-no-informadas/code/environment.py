from random import randrange
import math


class Node:
    position = None
    isObstacle = False
    status = 0  # 0 = unvisited. 1 = frontier. 2 = visited. 3 = path.
    prevNode = None
    distance = None

    def __init__(self, position):
        self.position = position  # position is a 2-tuple of int: (row, column)


class Environment:
    obstaclesRate = 0.2
    size = 20
    agent = None

    def __init__(self):
        self.matrix = [[Node((j, i)) for i in range(
            self.size)] for j in range(self.size)]  # Without obstacles
        self.__createObstacles()

    def __createObstacles(self):
        obstaclesLeft = math.ceil(
            self.obstaclesRate * self.size ** 2)
        while (obstaclesLeft > 0):
            row = randrange(self.size)
            column = randrange(self.size)
            alreadyHasObstacle = self.hasObstacle((row, column))
            if (not(alreadyHasObstacle)):
                self.matrix[row][column].isObstacle = True
                obstaclesLeft -= 1

    def getNodeAt(self, position):
        return self.matrix[position[0]][position[1]]

    def hasObstacle(self, position):
        return self.matrix[position[0]][position[1]].isObstacle

    def printEnvironment(self):
        for i in range(self.size):
            for j in range(self.size):
                node = self.matrix[i][j]
                if (node.isObstacle):
                    print(u"\u2B1C", end='')  # Obstáculo - blanco
                elif (self.agent != None and node == self.agent.initialNode):
                    print(" "u"\u25B7", end='')  # Origen
                elif (self.agent != None and node == self.agent.targetNode):
                    print(" "u"\u272A", end='')  # Objetivo
                elif (node.status == 2):
                    print("  ", end='')  # Explorado - negro
                elif (node.status == 3):
                    print(" =", end='')  # Camino
                else:
                    print(u"\u2B1B", end='')  # Inexplorado - gris
            print('')
        print('')
