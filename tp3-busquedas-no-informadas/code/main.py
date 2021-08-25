from agent import Agent
from environment import Environment

# env = Environment()

# agent = Agent(env, 2)
# env.printEnvironment()
iterations = 30

algorithms = ["BFS", "Búsqueda Uniforme", "DFS"]

for searchAlgo in range(len(algorithms)):
    successCount = 0
    statesCountsList = []
    media = 0
    DE = 0
    for i in range(iterations):
        env = Environment()
        agent = Agent(env, searchAlgo)
        performance = agent.getPerformance()
        statesCount = performance[0]
        success = performance[1] != None
        if (success):
            successCount += 1
            media += statesCount
            statesCountsList.append(statesCount)

    media = media / successCount

    for i in range(successCount):
        DE += (statesCountsList[i] - media) ** 2

    DE = round((DE / successCount) ** 0.5, 1)
    media = round(media, 1)

    print("\n-----------> Rendimiento del Agente usando el algoritmo",
          algorithms[searchAlgo])
    print(successCount, "de", iterations,
          "agentes tuvieron éxito en llegar al destino.")
    print("Media: ", media, "estados")
    print("Desviación Estándar: ", DE, "estados \n")
