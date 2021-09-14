from environment import Environment
from agents import hillClimbing, simulatedAnnealing

env = Environment(8, [1, 1, 2, 2, 2, 2, 6, 4])

print("\nInitial state: ")
env.print()

performance = simulatedAnnealing(env)

print("Threatened queens: ", performance[0])
if (performance[0] != 0):
    print("The threatened queens pairs are: ", performance[1])
env.print()
