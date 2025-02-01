def findTheLongestBinaryGap(value):
    maxBinaryGapLength = 0
    currentBinaryGapLength = 0
    hasOne = False

    while value != 0:
        remainder = value % 2
        value = value / 2
        if remainder == 1:
            hasOne = True
            if currentBinaryGapLength > maxBinaryGapLength:
                maxBinaryGapLength = currentBinaryGapLength
            currentBinaryGapLength = 0
        elif hasOne:
            currentBinaryGapLength += 1
    return maxBinaryGapLength