from src.game import *

# part 1
with open('./input1.txt', 'r') as file:
    print(checkGameFileForSumOfIdOnValidGames(file, [12,13,14]))

# part 2
with open('./input1.txt', 'r') as file:
    print(checkGameFileForPower(file))