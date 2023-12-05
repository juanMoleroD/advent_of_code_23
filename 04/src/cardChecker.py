def getCardPoints(input) -> int:
    parsedInput = input.split(":")[1].split('|')
    winningNums = parsedInput[0].split()
    nums = parsedInput[1].split()

    matchedNums = 0
    for num in nums:
        if num in winningNums:
            if matchedNums == 0: matchedNums += 1
            else: matchedNums *= 2
            
    return matchedNums

def getAllCardPoints(games) -> int:
    sum: int = 0
    for game in games:
        sum += getCardPoints(game)
    return sum

def getWiningDetails(game) -> int:
    parsedInput = game.split(":")[1].split('|')
    winningNums = parsedInput[0].split()
    nums = parsedInput[1].split()

    matchedNums = 0
    for num in nums:
        if num in winningNums:
            matchedNums += 1
    return matchedNums

def getCardCount(games) -> int:
    duplicates = []
    for num in range(len(games)):
        duplicates.append(1)

    for index, game in enumerate(games):
        details = getWiningDetails(game)
        for num in range(index + 1, index + 1 + details):
            duplicates[num] += 1 * duplicates[index]
            
    sum = 0
    for game in duplicates:
        sum += game

    return sum