from forwardchaining import ForwardChaining
from backtracking import Backtracking
from utils import printBoard
import time

forwardTimes = []
forwardStates = []
for size in [4, 8, 10, 12, 15]:
    startTime = time.time()
    result = ForwardChaining(size)
    endTime = time.time()
    if (result[0] != None):
        printBoard(result[0])
    forwardStates.append(result[1])
    forwardTimes.append(endTime - startTime)

print(forwardStates)
print(forwardTimes)

backtrackingTimes = []
backtrackingStates = []
for size in [4, 8, 10, 12, 15]:
    startTime = time.time()
    result = Backtracking(size)
    if (result[0] != None):
        printBoard(result[0])
    endTime = time.time()
    backtrackingStates.append(result[1])
    backtrackingTimes.append(endTime - startTime)

print(backtrackingStates)
print(backtrackingTimes)
