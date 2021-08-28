from dfsagent import AgentDFS
from uniformagent import AgentUniform
from bfsagent import AgentBFS
from agent import Agent
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
    algorithms = ["BFS", "Búsqueda Uniforme", "DFS"]

    for searchAlgo in range(len(algorithms)):
        statesCountsList = []
        for i in range(iterations):
            env = Environment()
            agent = Agent(env, searchAlgo)
            performance = agent.getPerformance()
            successful = performance[1] != None
            if (successful):
                statesCount = performance[0]
                statesCountsList.append(statesCount)

        successCount = len(statesCountsList)
        media = round(statistics.mean(statesCountsList), 1)
        DE = round(statistics.stdev(statesCountsList), 1)

        print("\n-----------> Rendimiento del Agente usando el algoritmo",
              algorithms[searchAlgo])
        print(successCount, "de", iterations,
              "agentes tuvieron éxito en llegar al destino.")
        print("Media: ", media, "estados")
        print("Desviación Estándar: ", DE, "estados \n")


# test() # Uncomment this line to run the 90 iterations for the different scenarios.
