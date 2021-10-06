class Environment:
    def __init__(self, size):
        self.size = size

    @staticmethod
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

    @staticmethod
    def print(queens):
        def icon(row, column):
            if (queens[row] != None and queens[row] == column):
                return u"\u2655" " "  # queen
            return u"\u25A2" " "  # empty slot

        size = len(queens)
        matrix = [[icon(row, column) for row in range(size)]
                  for column in range(size)]
        for i in range(size):
            for j in range(size):
                print(matrix[i][j], end='')
            print("")
        print("")
