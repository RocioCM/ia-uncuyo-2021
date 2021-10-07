def printBoard(queens):
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
