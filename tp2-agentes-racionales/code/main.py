from environment import Environment
from randomagent import RandomAgent
from reflexiveagent import ReflexiveAgent
import random

dirtRate = 0.1
sizes = [2, 4, 8, 16, 32, 64, 128]
dirtRates = [0.1, 0.2, 0.4, 0.8]

# # Agent performance:
# for size in sizes:
#     for dirt in dirtRates:
#         # Random Agent
#         print("Size: ", size, "x", size, ". Dirt: ", dirt)
#         env1 = Environment(size, size, dirt)

#         posX = random.randrange(size)
#         posY = random.randrange(size)
#         agent1 = RandomAgent(env1, posX, posY)
#         print(env1.getPerformance())

# Reflexive Agent
env2 = Environment(sizes[3], sizes[3], dirtRates[2])
print("Initial environment: ")
env2.printEnvironment()

posX = random.randrange(sizes[3])
posY = random.randrange(sizes[3])
print("Initial position: (" + str(posX) + ", " + str(posY) + "). \n")
agent2 = ReflexiveAgent(env2, posX, posY)
print("Final environment: ")
env2.printEnvironment()
print(env2.getPerformance())
