from environment import Environment
from math import ceil, factorial
import random

toString = lambda queens: ",".join(queens)

toArray = lambda individual: individual.split(",")

formatPopulationWithFitness = lambda population: list(
    map(lambda individual:
        (fitness(individual), toString(individual)), population))


def initPopulation(populationSize, individualSize):
    def Individual():
        return [
            str(random.randrange(individualSize))
            for i in range(individualSize)
        ]

    population = [Individual() for i in range(populationSize)]
    return formatPopulationWithFitness(population)


def fitness(individual):
    queens = individual
    threatened = 0
    for queen1 in range(len(queens)):
        for queen2 in range(queen1 + 1, len(queens)):
            threat = Environment.areQueensThreatening(
                (queen1, int(queens[queen1])), (queen2, int(queens[queen2])))
            if (threat):
                threatened += 1
    fitness = factorial(len(queens) - 1) + 1 - threatened
    return fitness  # Less threats means it's more fitting (so, a higher number is returned).


def reachedSolution(bestIndividual, size):
    if (bestIndividual == None):
        return False
    fitness = bestIndividual[0]
    if (fitness == factorial(size - 1) + 1):
        return True
    return False


def selectParentsWithProbability(population):
    parents = []
    populationCopy = population.copy()
    totalFitness = 0
    for individual in population:
        totalFitness += individual[0]
    for i in range(2):
        randomNumber = random.random()
        random.shuffle(populationCopy)
        parent = None
        while (parent == None):
            individual = populationCopy.pop()
            probabilityToReproduce = individual[0] / totalFitness
            if (randomNumber <= probabilityToReproduce):
                parent = individual
            elif ((i == 0 and len(populationCopy) == 1)
                  or (i == 1 and len(populationCopy) == 0)):
                parent = individual  #Only if no more parents are available.
        parents.append(toArray(parent[1]))
    return parents


def reproduce(parents, childrenNumber):
    [parent1, parent2] = parents
    children = []
    for i in range(childrenNumber // 2 + 1):
        splitIndex = random.randrange(len(parent1))
        child1 = parent1[0:splitIndex]
        child1.extend(parent2[splitIndex:len(parent2)])
        child2 = parent2[0:splitIndex]
        child2.extend(parent1[splitIndex:len(parent1)])
        children.extend([child1, child2])
    return children[0:childrenNumber]


def mutateWithProbability(individual, probability):
    randomNumber = random.random()
    if (randomNumber <= probability):
        index = random.randrange(len(individual))
        newValue = random.randrange(len(individual))
        individual[index] = str(newValue)
    return individual


def getBestNextGeneration(parents, children, splitPercent):
    size = len(parents)
    parents.sort(key=lambda tuple: tuple[0])
    children.sort(key=lambda tuple: tuple[0])
    # Keeps the best _splitPercent_ percentage of the previous generation and the other bests from the new generation.
    keptParents = parents[size - ceil(splitPercent * size):size]
    keptChildren = children[ceil(splitPercent * size):size]
    newPopulation = keptChildren
    newPopulation.extend(keptParents)
    return newPopulation


def genetic(queens):
    populationSize = 100
    maxTime = 200
    mutationProbability = 0.3
    splitPercent = 0.1
    childrenPerParents = 2

    #1. I create n random states. (each state is a string with 8 numbers from 0 to 7 separated by spaces, dots colons or whatever)
    population = initPopulation(populationSize, queens)
    population.sort(key=lambda tuple: tuple[0])
    time = 0
    best = None
    while (time < maxTime and not (reachedSolution(best, queens))):
        #1. Create the nextGeneration:
        children = []
        #2. For reproduction I choose n random pairs.
        for i in range(populationSize // childrenPerParents):
            #2.1 Each parent would be selected with probability proportional to their fitness.
            parents = selectParentsWithProbability(population)
            #3. From each pair of parents, I create a new pair (2) of children, not just one child.
            #3.1 Cut them at random index x and join both them.
            newChildren = reproduce(parents, childrenPerParents)
            children.extend(newChildren)
        #3.2. Each child has m probability of mutating a random position.
        for i in range(len(children)):
            child = children[i]
            children[i] = mutateWithProbability(child, mutationProbability)
        #4. I calculate the fitness for each new children (I mean, I calculate the threatened queens pairs count for each one).
        children = formatPopulationWithFitness(children)
        #5. Kill the worst (and keep the best from parents and children)
        population = getBestNextGeneration(population, children, splitPercent)
        #6. I order it (more fitting, more probability to reproduce. I mean, priority queue by fitness).
        population.sort(key=lambda tuple: tuple[0])
        #7. Of that population, keep the record of the best individual. So if the individual is fit enough (threatened=0, the loop stops, else, it will stop anyway after z iterations).
        bestOfGeneration = population[-1]  #The last item is the most fitting.
        if (time == 0 or best[0] < bestOfGeneration[0]):
            best = bestOfGeneration
        time += 1
    #8. Return the record of the best individual you got across the whole algorithm (that is not necessary the last best, just the best across all).
    return (factorial(queens - 1) + 1 - best[0], toArray(best[1]), time)


# print(fitness("1,3,2,4"))

# print(initPopulation(3, 4))

print(genetic(8))
# genetic(100, 8, 1000, 0.3, 0.1, 2)

# print(
#     getBestNextGeneration([(3, '1,1,1,2'), (3, '2,2,2,0'), (1, '0,2,1,2')],
#                           [(3, ''), (2, ''), (4, '')], 0.1))

# print(reproduce(([1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2]), 7))
