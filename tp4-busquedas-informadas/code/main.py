from agent import Agent
from environment import Environment
import statistics

print("Ejemplo: ")
env = Environment()
agent = Agent(env)
env.printEnvironment()
performance = agent.getPerformance()
print("Cantidad de estados: ", performance[0])
print("Sucesión de estados: ", performance[1])


def test():
    iterations = 100
    statesCountsList = []
    for i in range(iterations):
        env = Environment()
        agent = Agent(env)
        performance = agent.getPerformance()
        successful = performance[1] != None
        if (successful):
            statesCount = performance[0]
            statesCountsList.append(statesCount)

    successCount = len(statesCountsList)
    media = round(statistics.mean(statesCountsList), 1)
    DE = round(statistics.stdev(statesCountsList), 1)

    print("\n-----------> Rendimiento del Agente")
    print(successCount, "de", iterations,
          "agentes tuvieron éxito en llegar al destino.")
    print("Media: ", media, "estados")
    print("Desviación Estándar: ", DE, "estados \n")


test()  # Uncomment this line to run the 30 iterations.
