import math
import random


def hillClimbing(env):
    return Agent(env, lambda *args: False)


def simulatedAnnealing(env):
    def chooseWorseState(count, nextCount, T):
        dE = nextCount - count
        probability = math.e**(
            dE / T)  # ///This now greater than 1. It should be [0,1].
        print("Probability: ", probability)  # ///
        randomNumber = random.random()
        return randomNumber <= probability

    return Agent(env, chooseWorseState)


def Agent(env, chooseStateWithProbability):
    cont = 0
    threatenedQueens = env.getThreatenedQueensPairsCount()  #int
    while threatenedQueens != 0:
        cont += 1
        nextStates = env.getAllPossibleNextStates()
        # nextStates: (int, (int, int))[] # nextState is an Array of tuples containing the count of threatened queens in that state and the movement to reach that state: (queenColumn, moveToRow).
        nextStates.sort(key=(lambda state: state[0]), reverse=True)
        # state[0] is the number of threatened queens pairs in that state.
        nextState = nextStates.pop()
        [nextThreatenedQueens, movement] = nextState
        if (threatenedQueens <=
                nextThreatenedQueens):  #The new state is worse.
            useTheNextState = chooseStateWithProbability(
                threatenedQueens, nextThreatenedQueens, cont)
            if (not (useTheNextState)):
                break
        env.moveQueen(movement)
        threatenedQueens = nextThreatenedQueens

    print(("Solution found", "Found partial solution")[threatenedQueens != 0])
    print("Iterations: ", cont)
    return (threatenedQueens, env.getThreatenedQueensList())
