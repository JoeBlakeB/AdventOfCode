#!/usr/bin/env python3

# Advent of Code 2023 - Day 2: Cube Conundrum
# Usage:
#     python 2023/02-Cube-Conundrum.py < 2023/inputs/02.txt

import fileinput
inputSplit = [line.strip() for line in list(fileinput.input())]

def getCubeCountsPerGame(inputSplit: list[str]) -> list[tuple[int, int, int]]:
    cubeCountsPerGame = []
    for line in inputSplit:
        r, g, b = 0, 0, 0
        sets = line.split(": ")[1].split("; ")
        for set in sets:
            colourCounts = set.split(", ")
            for colourCount in colourCounts:
                count, colour = colourCount.split(" ")
                if colour[0] == "r":
                    r = max(r, int(count))
                elif colour[0] == "g":
                    g = max(g, int(count))
                elif colour[0] == "b":
                    b = max(b, int(count))
                else:
                    raise Exception(count, colour)
        cubeCountsPerGame.append((r, g, b))
    return cubeCountsPerGame


maxCounts = (12, 13, 14)
allCubeCounts = getCubeCountsPerGame(inputSplit)
possibleGameSum = 0
gamePowerSum = 0

for gameID, cubeCounts in enumerate(allCubeCounts, 1):
    if not any(cubes > maxCubes for cubes, maxCubes in zip(cubeCounts, maxCounts)):
        possibleGameSum += gameID

    r, g, b = cubeCounts
    gamePowerSum += r*g*b

print("Sum of IDs of possible games:", possibleGameSum)
print("Sum of game powers:", gamePowerSum)
