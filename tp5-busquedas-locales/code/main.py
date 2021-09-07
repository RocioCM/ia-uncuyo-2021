from environment import Environment
from agents import hillClimbing, simulatedAnnealing


env = Environment(8, [1, 1, 2,2,2,2,6,4]) 

performance = hillClimbing(env)
print(performance)