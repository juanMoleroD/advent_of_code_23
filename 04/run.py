from src.cardChecker import *

games = []

with open('./input.txt','r') as file:
    for line in file:
        games.append(line.strip())

# Pard 1
print(getAllCardPoints(games))

# Part 2
print(getCardCount(games))
