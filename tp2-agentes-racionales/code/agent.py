from abc import ABC, abstractmethod


class Agent(ABC):
    remainingActions = 1000
    points = 0

    def __init__(self, environment, initPosX, initPosY):
        self.environment = environment
        if initPosX < 0 or initPosX > environment.size[0] - 1 or initPosY < 0 or initPosY > environment.size[1] - 1:
            raise Exception('Initial position out of index')
        self.positionX = initPosX
        self.positionY = initPosY
        print('Initial position: (', initPosX, ',', initPosY, ') \n')
        while (self.remainingActions > 0):
            self.think()

    def up(self):
        if (self.positionY > 0):
            self.positionY -= 1
        self.remainingActions -= 1

    def down(self):
        if (self.positionY < self.environment.size[1] - 1):
            self.positionY += 1
        self.remainingActions -= 1

    def left(self):
        if (self.positionX > 0):
            self.positionX -= 1
        self.remainingActions -= 1

    def right(self):
        if (self.positionX < self.environment.size[0] - 1):
            self.positionX += 1
        self.remainingActions -= 1

    def suck(self):
        if (self.perceive()):
            self.points += 1
        self.environment.dispatchAction(
            'clean', self.positionX, self.positionY)
        self.remainingActions -= 1

    def idle(self):
        self.remainingActions -= 1

    def perceive(self):
        return self.environment.isDirty(self.positionX, self.positionY)

    @abstractmethod
    def think(self):
        pass
