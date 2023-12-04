def findPotentialPart(lines: []) -> {}:
    partX: int = -1
    partY: int = -1
    partLen: int = -1
    for linesIndex, line in enumerate(lines):
        partFound = False
        for charIndex, char in enumerate(line):
            if char != '.' and partFound == True:
                partLen += 1
            if char != '.' and partFound == False:
                partFound = True
                partX = charIndex
                partY = linesIndex
                partLen = 1
            if char == '.' and partFound == True: 
                break 
    value: int = int(lines[partY][partX:(partX + partLen)])
    return { "partX": partX, "partY": partY, "partLen": partLen , "value": value}

def checkIfPart(potentialPart: {}, lines: []):
    # check sides
    sides = []
    leftChar: str = lines[potentialPart["partY"]][potentialPart["partX"] - 1]
    rightChar: str = lines[potentialPart["partY"]][potentialPart["partX"] + potentialPart["partLen"]]
    sides.append(leftChar)
    sides.append(rightChar)

    for side in sides:
        if checkIfPartSymbol(side):
            return True
    return False

def checkIfPartSymbol(char: str) -> bool:
    return char != '.' and char.isalpha() == False
