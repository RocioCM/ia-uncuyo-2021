class Environment:
    def __init__(self, sizeX, sizeY, dirtRate):
        self.size = (sizeX, sizeY)
        self.matrix = [[1 for i in range(sizeX)] for j in range(sizeY)]
        if (dirtRate < 0 or dirtRate > 1):
            raise Exception('Dirt rate must be in range [0,1]')
        self.initialDirtRate = dirtRate
        self.dirtRate = dirtRate
        # Inicializar el tablero con mugre aleatoria en base al dirt rate.
        print("Hola")

    def dispatchAction(self, action, posX, posY):
        if (action == 'clean'):
            if (self.isDirty(posX, posY)):
                self.dirtRate = (
                    (self.dirtRate * self.size[0] * self.size[1]) - 1) / (self.size[0] * self.size[1])
                self.matrix[posY][posX] = 0

    def isDirty(self, posX, posY):
        return self.matrix[posY][posX] == 1

    def getPerformance(self):
        return (1 - self.dirtRate / self.initialDirtRate)

    def printEnvironment(self):
        for i in range(self.size[1]):
            print(self.matrix[i])
        print('')
