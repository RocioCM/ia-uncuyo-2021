from agent import Agent
from random import randrange


class RandomAgent(Agent):
    def think(self):
        action = randrange(6)
        if (action == 0):
            self.up()
        elif (action == 1):
            self.down()
        elif (action == 2):
            self.left()
        elif (action == 3):
            self.right()
        elif (action == 4):
            self.suck()
        elif (action == 5):
            self.idle()
