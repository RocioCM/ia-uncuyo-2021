from environment import Environment
from agents import hillClimbing, simulatedAnnealing

env = Environment(8, [1, 1, 1, 1, 1, 1, 1, 1])

print("\nInitial state: ")
env.print()

performance = hillClimbing(env)

print("Threatened queens pairs: ", performance[0])
if (performance[0] != 0):
    print(
        "The threatened queens pairs are (the numbers are zero-based queens columns): ",
        performance[1])
env.print()
