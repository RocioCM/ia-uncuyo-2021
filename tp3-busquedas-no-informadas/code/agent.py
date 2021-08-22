from random import randrange


class Agent:
    def __init__(self, environment):
        self.environment = environment
        availableStartPosition = False
        while (not(availableStartPosition)):
            initPosX = randrange(environment.size)
            initPosY = randrange(environment.size)
            if (not(environment.hasObstacle(initPosY, initPosX))):
                availableStartPosition = True
        self.positionX = initPosX
        self.positionY = initPosY
        self.think()

    def up(self):
        if (self.positionY > 0):
            self.positionY -= 1

    def down(self):
        if (self.positionY < self.environment.size - 1):
            self.positionY += 1

    def left(self):
        if (self.positionX > 0):
            self.positionX -= 1

    def right(self):
        if (self.positionX < self.environment.size - 1):
            self.positionX += 1

    def perceive(self):
        print("Hola")

    def think(self):
        print("Hola")
