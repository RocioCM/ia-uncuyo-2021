from agent import Agent
import random
from environment import Environment

env = Environment()
# env.printEnvironment()

iterations = 30
successCount = 0
statesCountsList = []
media = 0
DE = 0

for i in range(iterations):
    # env = Environment()
    # agent = Agent(env)
    success = True  # Hola
    statesCount = i  # Hola
    if (success):
        successCount += 1
        media += statesCount
        statesCountsList.append(statesCount)

media = media / successCount

for i in range(successCount):
    DE += (statesCountsList[i] - media) ** 2

DE = round((DE / successCount) ** 0.5, 1)
media = round(media, 1)

print(successCount, "de", iterations,
      "agentes tuvieron éxito en llegar al destino.")
print("Media: ", media, "estados")
print("Desviación Estándar: ", DE, "estados")
