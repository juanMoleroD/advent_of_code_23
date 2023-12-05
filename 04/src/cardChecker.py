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