lowerBound = '236491'
upperBound = '713787'
numOfPasswordsP1 = 0
numOfPasswordsP2 = 0
testPassword = lowerBound

while int(testPassword) <= int(upperBound):
    isAdjacent = False
    isIncreasing = True
    isSingleAdjacent = False
    numAdjacentMax = 0
    numAdjacentMin = 0
    for i in range(1, len(testPassword)):
        if int(testPassword[i]) == int(testPassword[i-1]):
            isAdjacent = True
        if int(testPassword[i]) < int(testPassword[i-1]):
            isIncreasing = False
    
    if isAdjacent & isIncreasing:
        digits = {}
        for digit in testPassword:
            digits[str(digit)] = digits.get(str(digit), 0) + 1
        for amount in digits.values():
            if amount == 2:
                isSingleAdjacent = True
    
    if isAdjacent & isIncreasing:
        numOfPasswordsP1 += 1
    if isAdjacent & isIncreasing & isSingleAdjacent:
        numOfPasswordsP2 += 1
        
    testPassword = str(int(testPassword)+1)

print('Eligible passwords P1: ', numOfPasswordsP1)
print('Eligible passwords P2: ', numOfPasswordsP2)
