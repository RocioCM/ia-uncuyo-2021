from random import shuffle

def getRandomState(size):
	newState = [i for i in range(size)]
	shuffle(newState)
	return newState