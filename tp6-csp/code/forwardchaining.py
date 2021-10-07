from copy import deepcopy


def forwardChecking(queenStart, row, matrix):
    diagonal1 = row
    diagonal2 = row
    for queen in range(queenStart, len(matrix)):
        diagonal1 -= 1
        diagonal2 += 1
        column = matrix[queen]
        if (len(column) == 0):
            return False
        if (row in column):
            column.remove(row)
        if (diagonal1 >= 0 and (diagonal1 in column)):
            column.remove(diagonal1)
        if (diagonal2 < len(matrix) and (diagonal2 in column)):
            column.remove(diagonal2)

    for column in matrix:
        if (len(column) == 0):
            return False
    return True


def recursiveForward(queen, row, matrix, states):
    if (queen + 1 == len(matrix)):
        return [row]

    checked = forwardChecking(queen + 1, row, matrix)
    if (checked):
        nextColumn = matrix[queen + 1]
        if (len(nextColumn) == 0):
            return None
        for nextRow in nextColumn:
            states[0] += 1
            result = recursiveForward(queen + 1, nextRow, deepcopy(matrix),
                                      states)
            if (not (not (result))):
                result.append(row)
            if (result == None):
                continue
            return result
    return None


def ForwardChaining(size):
    states = [0]
    matrix = [[j for j in range(size)] for i in range(size)]
    for row in matrix[0]:
        result = recursiveForward(0, row, matrix, states)
        if (not (not (result))):
            result.reverse()
            return (result, states[0])
    return (None, states[0])
