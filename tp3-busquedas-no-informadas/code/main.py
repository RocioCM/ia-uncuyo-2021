from dfsagent import AgentDFS
from uniformagent import AgentUniform
from bfsagent import AgentBFS
from environment import Environment
import statistics

print("Ejemplo usando DFS: ")
env = Environment()
agent = AgentDFS(env)
env.printEnvironment()
performance = agent.getPerformance()
print("Cantidad de estados: ", performance[0])
print("Sucesión de estados: ", performance[1])


def test():
    iterations = 30
    algorithms = [("BFS", AgentBFS),
                  ("Búsqueda Uniforme", AgentUniform),
                  ("DFS", AgentDFS)]

    for agentType in algorithms:
        statesCountsList = []
        for i in range(iterations):
            env = Environment()
            agent = agentType[1](env)
            performance = agent.getPerformance()
            successful = performance[1] != None
            if (successful):
                statesCount = performance[0]
                statesCountsList.append(statesCount)

        successCount = len(statesCountsList)
        media = round(statistics.mean(statesCountsList), 1)
        DE = round(statistics.stdev(statesCountsList), 1)

        print("\n-----------> Rendimiento del Agente usando el algoritmo",
              agentType[0])
        print(successCount, "de", iterations,
              "agentes tuvieron éxito en llegar al destino.")
        print("Media: ", media, "estados")
        print("Desviación Estándar: ", DE, "estados \n")


# Uncomment this line to run the 90 iterations for the different scenarios.
test()
