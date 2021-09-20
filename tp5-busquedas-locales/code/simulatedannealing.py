import random


def simulatedAnnealing(env):
    maxTime = 200
    time = 0
    threatenedQueens = env.getThreatenedQueensPairsCount()  #int
    while (threatenedQueens != 0 and time < maxTime):
        time += 1
        movement = None
        while (movement == None or env.queens[movement[0]] == movement[1]):
            movement = (random.randrange(env.size), random.randrange(env.size))
        nextThreatenedQueens = len(
            env.getThreatenedQueensForMovement(movement))
        if (threatenedQueens <= nextThreatenedQueens):  #The new state is worse
            probability = 1 / time  # More time, less probability
            randomNumber = random.random()
            if (randomNumber > probability):
                #The worse state is not selected.
                continue
        env.moveQueen(movement)
        threatenedQueens = nextThreatenedQueens

    print(("Solution found", "Found partial solution")[threatenedQueens != 0])
    print("Iterations: ", time)
    return (threatenedQueens, env.getThreatenedQueensList(), time)
