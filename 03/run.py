from src.partReader import *

input = []
with open('./input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

# part 1
print(checkPartsAndGetSumOfCorrectParts(input))

# part 2
print(getGearsRatioSum(input))
#not 58632351
