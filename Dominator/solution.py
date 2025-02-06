from array import *

def findADominatorIndex(values):
    copiedValues = values.copy()
    values.sort()

    count = 1
    for i in range(len(values)):
        if i != 0 and values[i] == values[i - 1]:
            count += 1
        else:
            count = 1

        if count > len(values) / 2:
            for j in range(len(values)):
                if copiedValues[j] == values[i]:
                    return j
    return -1
    