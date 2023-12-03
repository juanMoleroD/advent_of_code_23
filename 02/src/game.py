class game():
    def __init__(self, id:int, rounds: []):
        self.id:int = id
        self.rounds = rounds

def gameFactory(input: str) -> game:
    parsedId: int = int(input[5])
    parsedRounds = []
    result = game(parsedId, parsedRounds)
    return result


def checkCubes(numOfReds: int, numOfGreens: int, numOfBlues: int, input: str) -> bool:
    removeGameId = input.split(':')[1]
    rounds = removeGameId.split(";")
    inputs = []
    for round in rounds:
        inputs.append(round.split(','))
    # print(inputs)

    for round in inputs:
        for input in round:
            if input[-1] == 'd': # as in reD
                num = input.split(' ')[1]
                if int(num) > numOfReds: 
                    return False
            if input[-1] == 'n': # as in greeN
                num = input.split(' ')[1]
                if int(num) > numOfGreens: 
                    return False
            if input[-1] == 'e': # as in bluE
                num = input.split(' ')[1]
                # print(f'if num {num} > {numOfReds} return false')
                if int(num) > numOfBlues: 
                    return False
    return True