from environment import Environment
from randomagent import RandomAgent
from reflexiveagent import ReflexiveAgent
import random

sizeX = 12
sizeY = 12
dirtRate = 0.5

# Random Agent
env1 = Environment(sizeX, sizeY, dirtRate)
env1.printEnvironment()

posX = random.randrange(sizeX)
posY = random.randrange(sizeY)
agent1 = RandomAgent(env1, posX, posY)
agent1.suck()
env1.printEnvironment()
print(env1.getPerformance())

# Reflexive Agent
env2 = Environment(sizeX, sizeY, dirtRate)
env2.printEnvironment()

posX = random.randrange(sizeX)
posY = random.randrange(sizeY)
agent2 = ReflexiveAgent(env2, posX, posY)
agent2.suck()
env2.printEnvironment()
print(env2.getPerformance())
