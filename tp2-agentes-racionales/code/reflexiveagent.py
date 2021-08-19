from agent import Agent
from random import randrange


class ReflexiveAgent(Agent):
    def think(self):
        if (self.perceive()):
            self.suck()
        else:
            action = randrange(4)
            if (action == 0):
                self.up()
            elif (action == 1):
                self.down()
            elif (action == 2):
                self.left()
            elif (action == 3):
                self.right()
