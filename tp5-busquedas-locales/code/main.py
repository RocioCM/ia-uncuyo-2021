from environment import Environment
from hillclimbing import hillClimbing
from simulatedannealing import simulatedAnnealing
from genetic import genetic
import time

for size in [4, 8, 10, 12, 15]:
    hillTimes = []
    simulatedTimes = []
    geneticTimes = []
    for i in range(30):
        initialState = Environment.getRandomState(size)
        startTime = time.time()
        env = Environment(size, initialState)
        performance = simulatedAnnealing(env)
        endTime = time.time()
        simulatedTimes.append(endTime - startTime)

        startTime = time.time()
        env = Environment(size, initialState)
        performance = hillClimbing(env)
        endTime = time.time()
        hillTimes.append(endTime - startTime)

        startTime = time.time()
        performance = genetic(size)
        endTime = time.time()
        geneticTimes.append(endTime - startTime)
    print("\n\n\n")
    print("Hill for size ", size, ": ", hillTimes)
    print("Simulated for size ", size, ": ", simulatedTimes)
    print("Genetic for size ", size, ": ", geneticTimes)

# # Code for just one execution:
# env = Environment(15)
# print("\nInitial state: ")
# env.print()
# performance = simulatedAnnealing(env)
# print("Threatened queens pairs: ", performance[0])
# if (performance[0] != 0):
#     print(
#         "The threatened queens pairs are (the numbers are zero-based queens columns): ",
#         performance[1])
# env.print()
