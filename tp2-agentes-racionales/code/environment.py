from random import randrange
import math


class Environment:
    dirtRate = 0

    def __init__(self, sizeX, sizeY, dirtRate):
        self.size = (sizeX, sizeY)
        self.matrix = [[0 for i in range(sizeX)] for j in range(sizeY)]
        if (dirtRate < 0 or dirtRate > 1):
            raise Exception('Dirt rate must be in range [0,1]')
        self.initialDirtRate = dirtRate
        self.__createDirty()

    def __createDirty(self):
        tilesLeftToDirty = math.ceil(
            self.initialDirtRate * self.size[0] * self.size[1])
        while (tilesLeftToDirty > 0):
            column = randrange(self.size[0])
            row = randrange(self.size[1])
            isTileDirty = self.isDirty(column, row)
            if (not(isTileDirty)):
                self.dispatchAction('dirty', column, row)
                tilesLeftToDirty -= 1

    def dispatchAction(self, action, posX, posY):
        if (action == 'clean'):
            if (self.isDirty(posX, posY)):
                self.dirtRate = (
                    (self.dirtRate * self.size[0] * self.size[1]) - 1) / (self.size[0] * self.size[1])
                self.matrix[posY][posX] = 0
        elif (action == 'dirty'):
            if (not(self.isDirty(posX, posY))):
                self.dirtRate = (
                    (self.dirtRate * self.size[0] * self.size[1]) + 1) / (self.size[0] * self.size[1])
                self.matrix[posY][posX] = 1

    def isDirty(self, posX, posY):
        return self.matrix[posY][posX] == 1

    def getPerformance(self):
        if (self.initialDirtRate != 0):
            percentCleaned = (1 - self.dirtRate / self.initialDirtRate)
        else:
            percentCleaned = 1
        cleanedTiles = math.floor(percentCleaned * math.ceil(
            self.initialDirtRate * self.size[0] * self.size[1]))
        return "Cleaned " + str(round(percentCleaned*100, 2)) + "% (" + str(cleanedTiles) + " tiles) of the initial dirt. \n"

    def printEnvironment(self):
        for i in range(self.size[1]):
            print(self.matrix[i])
        print('')
