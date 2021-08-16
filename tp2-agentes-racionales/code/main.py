from environment import Environment
from randomagent import RandomAgent
import random

sizeX = 12
sizeY = 12
dirtRate = 1
env1 = Environment(sizeX, sizeY, dirtRate)
env1.printEnvironment()


posX = random.randrange(sizeX)
posY = random.randrange(sizeY)
agent1 = RandomAgent(env1, posX, posY)
agent1.suck()
env1.printEnvironment()
print(env1.getPerformance())
