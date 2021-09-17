from environment import Environment
from hillclimbing import hillClimbing
from simulatedannealing import simulatedAnnealing

env = Environment(8, [4, 5, 6, 3, 4, 5, 6, 5])

print("\nInitial state: ")
env.print()

# performance = hillClimbing(env)
performance = simulatedAnnealing(env)

print("Threatened queens pairs: ", performance[0])
if (performance[0] != 0):
    print(
        "The threatened queens pairs are (the numbers are zero-based queens columns): ",
        performance[1])
env.print()
