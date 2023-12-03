def checkCubes(numOfReds: int, numOfGreens: int, numOfBlues: int, input: str) -> bool:
    game = input.split(':')
    rounds = game[1].split(";")
    inputs = []
    for round in rounds:
        inputs.append(round.split(','))
    for round in inputs:
        for input in round:
            if input[-1] == 'd': # as in reD
                num = input.split(' ')[1]
                if int(num) > numOfReds: 
                    return 0
            if input[-1] == 'n': # as in greeN
                num = input.split(' ')[1]
                if int(num) > numOfGreens: 
                    return 0
            if input[-1] == 'e': # as in bluE
                num = input.split(' ')[1]
                if int(num) > numOfBlues: 
                    return 0
    return int(game[0].split(" ")[1])

def checkGameFile(file, numOfRGBCubes: []) -> int:
    sum: int = 0
    for line in file:
        sum += checkCubes(numOfRGBCubes[0], numOfRGBCubes[1], numOfRGBCubes[2], line.strip())
    return sum

def getMinimunCubes(input: str) -> []:
    minimumRed = 0
    minimunGreen = 0
    minimunBlue = 0
    game = input.split(':')
    rounds = game[1].split(';')
    inputs = []
    for round in rounds:
        inputs.append(round.split(','))
    for round in inputs:
        for input in round:
            print(input)
            if input[-1] == 'd': # as in reD
                num = input.split(' ')[1]
                if int(num) > minimumRed:
                    minimumRed = int(num) 
            if input[-1] == 'n': # as in greeN
                num = input.split(' ')[1]
                if int(num) > minimunGreen: 
                    minimunGreen = int(num)
            if input[-1] == 'e': # as in bluE
                print(f'blue found - input is {input}')
                num = input.split(' ')[1]
                print(f'if num {num} > {minimunBlue} set minBlue to {num}')
                if int(num) > minimunBlue: 
                    minimunBlue = int(num)
    
    return [minimumRed, minimunGreen, minimunBlue]