from environment import Environment


def recursiveBacktrack(queens, size, states):
    states[0] += 1
    for i in range(size):
        if (i not in queens):
            queens.append(i)
            h = Environment.calculateThreats(queens)
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
