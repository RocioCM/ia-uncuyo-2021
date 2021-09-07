import math
import random


def hillClimbing(env):
	def chooseWorseState(prev, current, cont):
		return False

	return Agent(env, chooseWorseState)

def simulatedAnnealing(env):
	def chooseWorseState(count, nextCount, T):
		dE = nextCount - count
		probability = math.e ** (dE/T)
		print("Probability: ", probability) # ///
		randomNumber = random.random()
		return randomNumber >= probability

	return Agent(env, chooseWorseState)

def Agent(env, chooseStateWithProbability):
	cont = 0
	threatenedQueens = env.getThreatenedQueensPairsCount()
	while True:
		cont += 1
		nextStates = env.getAllPossibleNextStates() # [(int, (int, int))] # Arreglo de tuplas con cantidad de reinas amenazadas y movimiento para llegar a ese estado (queenColumn, moveToRow)
		nextStates.sort(key = (lambda state: state[0]), reverse=True) # state[0] is the number of threatened queens pairs in that state.
		nextState = nextStates.pop()
		[nextThreatenedQueens, movement] = nextState
		if (threatenedQueens < nextThreatenedQueens):
			useTheNextState = chooseStateWithProbability(threatenedQueens, nextThreatenedQueens, cont)
			if (not(useTheNextState)):
				print("Iterations: ", cont) # ///
				env.print()
				return (threatenedQueens, env.getThreatenedQueensList())
		env.moveQueen(movement)
		threatenedQueens = nextThreatenedQueens
