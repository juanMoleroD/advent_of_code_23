def findPotentialParts(lines: []) -> {}:
    result: [] = []
    partX: int = -1
    partY: int = -1
    partLen: int = -1
    for linesIndex, line in enumerate(lines):
        partFound = False
        for charIndex, char in enumerate(line):
            if char.isnumeric() and partFound == True:
                partLen += 1
            if char.isnumeric() and char != '.':
                if partFound == False:
                    partFound = True
                    partX = charIndex
                    partY = linesIndex
                    partLen = 1
            if (char == '.' or not char.isnumeric()) and partFound == True: 
                value: int = int(lines[partY][partX:(partX + partLen)])
                result.append({ "partX": partX, 
                                "partY": partY, 
                                "partLen": partLen , 
                                "value": value})
                partX: int = -1
                partY: int = -1
                partLen: int = -1
                partFound = False
        if partFound: # for if last digit is part
            value: int = int(lines[partY][partX:(partX + partLen)])
            result.append({ "partX": partX, 
                            "partY": partY, 
                            "partLen": partLen , 
                            "value": value})
            partX: int = -1
            partY: int = -1
            partLen: int = -1
            partFound = False

    return result

def checkIfPart(potentialPart: {}, lines: []) -> bool:
    # on edge?
    onLeftEdge: bool = potentialPart["partX"] == 0
    onRightEdge: bool = potentialPart["partX"] + potentialPart["partLen"] == len(lines[potentialPart["partY"]])
    onBottomEdge: bool = potentialPart["partY"] == len(lines) - 1
    onTopEdge: bool = potentialPart["partY"] == 0

    validPartIndexMostLeft: int = potentialPart["partX"]
    if not onLeftEdge:
        validPartIndexMostLeft -= 1
    validPartIndexMostRight: int = potentialPart["partX"] + potentialPart["partLen"]
    if not onRightEdge:
        validPartIndexMostRight += 1
    sides = []
    if not onLeftEdge: 
        leftChar: str = lines[potentialPart["partY"]][potentialPart["partX"] - 1]
        sides.append(leftChar)
    if not onRightEdge:
        rightChar: str = lines[potentialPart["partY"]][potentialPart["partX"] + potentialPart["partLen"]]
        sides.append(rightChar)
    # top & bottom
    for value in range(validPartIndexMostLeft, validPartIndexMostRight):
        if not onTopEdge: sides.append(lines[potentialPart["partY"] - 1][value])
        if not onBottomEdge: sides.append(lines[potentialPart["partY"] + 1][value])

    for side in sides:
        if checkIfPartSymbol(side):
            return True
    return False

def checkIfPartSymbol(char: str) -> bool:
    return char != '.' and char.isalpha() == False

def checkPartsAndGetSumOfCorrectParts(potentialParts: [], input):
    sum: int = 0
    for part in potentialParts:
        if checkIfPart(part, input):
            sum += part["value"]
    return sum