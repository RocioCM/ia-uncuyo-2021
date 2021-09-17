from random import shuffle


class Environment:
    def __init__(self, size, initState=None):
        self.size = size
        if (initState == None):
            initState = self.getRandomState(size)
        elif (not (self.__isValidState(initState))):
            raise Exception(
                "Provided initial state is not a valid state for this environment"
            )
        self.queens = initState
        self.calculateAllThreats()

    @staticmethod
    def getRandomState(size):
        newState = [i for i in range(size)]
        shuffle(newState)
        return newState

    @staticmethod
    def areQueensThreatening(queen1, queen2):
        [queen1Col, queen1Row] = queen1
        [queen2Col, queen2Row] = queen2
        if (queen1Col == queen2Col):  # same column
            return True
        if (queen1Row == queen2Row):  # same row
            return True
        if (abs(queen1Col - queen2Col) == abs(queen1Row -
                                              queen2Row)):  # same diagonal
            return True
        return False

    def __isValidState(self, state):
        if (len(state) != self.size):
            return False
        for i in range(self.size):
            if (state[i] < 0 or state[i] >= self.size):
                return False
        return True

    def getThreatenedQueensPairsCount(self):
        return len(self.threatenedQueens)

    def getThreatenedQueensList(self):
        return self.threatenedQueens

    def calculateAllThreats(self):
        threatenedPairs = []
        for queen1 in range(self.size):
            for queen2 in range(queen1 + 1, self.size):
                if (queen1 != queen2):
                    threat = self.areQueensThreatening(
                        (queen1, self.queens[queen1]),
                        (queen2, self.queens[queen2]))
                    if (threat):
                        threatenedPairs.append((queen1, queen2))
        self.threatenedQueens = threatenedPairs

    def moveQueen(self, movement):
        [queenColumn, newRow] = movement
        self.queens[queenColumn] = newRow
        self.threatenedQueens = self.getThreatenedQueensForMovement(movement)

    def getAllPossibleNextStates(self):
        nextStates = []
        for column in range(self.size):
            for row in range(self.size):
                if (self.queens[column] != row):
                    nextPairs = self.getThreatenedQueensForMovement(
                        (column, row))
                    nextStates.append((len(nextPairs), (column, row)))
        return nextStates

    def getThreatenedQueensForMovement(self, movement):
        queenColumn = movement[0]
        newThreatened = self.threatenedQueens.copy()
        # 1. Delete from threatened all tuples where the first or the second value (queen) is queenColumn.
        for i in range(len(newThreatened) - 1, -1, -1):
            pair = newThreatened[i]
            if (pair[0] == queenColumn or pair[1] == queenColumn):
                newThreatened.remove(pair)
        # 2. Recalculate the threat from that queen to the other n-1 queens and push them to the array.
        for otherQueen in range(self.size):
            if (otherQueen != queenColumn):
                threat = self.areQueensThreatening(
                    movement, (otherQueen, self.queens[otherQueen]))
                if (threat):
                    newThreatened.append((queenColumn, otherQueen))
        return newThreatened

    def print(self):
        def icon(row, column):
            if (self.queens[row] == column):
                return u"\u2655" " "  # queen
            return u"\u25A2" " "  # empty slot

        size = self.size
        matrix = [[icon(row, column) for row in range(size)]
                  for column in range(size)]
        for i in range(size):
            for j in range(size):
                print(matrix[i][j], end='')
            print("")
        print("")
