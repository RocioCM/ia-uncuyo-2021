def calculateThreats(queens):
    cont = 0
    size = len(queens)
    for queen1 in range(size):
        for queen2 in range(queen1 + 1, size):
            if (queen1 == queen2):  # same column
                cont += 1
            elif (queens[queen1] == queens[queen2]):  # same row
                cont += 1
            elif (abs(queen1 -
                      queen2) == abs(queens[queen1] -
                                     queens[queen2])):  # same diagonal
                cont += 1
    return cont


def recursiveBacktrack(queens, size, states):
    states[0] += 1
    for i in range(size):
        if (i not in queens):
            queens.append(i)
            h = calculateThreats(queens)
            if (h == 0):
                if (len(queens) == size):
                    return queens
                result = recursiveBacktrack(queens, size, states)
                if (result != None):
                    return result
            queens.pop()
    return


def Backtracking(size):
    states = [0]
    queens = recursiveBacktrack([], size, states)
    return (queens, states[0])
