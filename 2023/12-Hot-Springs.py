#!/usr/bin/env python3

# Advent of Code 2023 - Day 12: Hot Springs
# Usage:
#     python 2023/12-Hot-Springs.py < 2023/inputs/12.txt

import sys
from itertools import product


INPUT_LINES = [line.strip() for line in sys.stdin if line.strip()]


def isArrangementPossible(arrangement: list[str], damagedGroups: list[int]) -> bool:
    thisArrangementsGroups = [0]
    for char in arrangement:
        if char == "#":
            thisArrangementsGroups[-1] += 1
        elif thisArrangementsGroups[-1]:
            thisArrangementsGroups.append(0)
    
    if not thisArrangementsGroups[-1]:
        thisArrangementsGroups.pop(-1)
    
    return thisArrangementsGroups == damagedGroups


def getNumberOfDifferentArrangements(line: str) -> int:
    damagedGroups: list[int] = [int(num) for num in line.split()[1].split(",")]
    springsString = line.split()[0]
    springsList = []
    unknownSpringsCount = 0
    for spring in springsString:
        if spring == "?":
            springsList.append(unknownSpringsCount)
            unknownSpringsCount += 1
        else:
            springsList.append(spring)
    
    possibleCombinations = 0
    for possibleSprings in product(".#", repeat=unknownSpringsCount):
        possibleCombinations += isArrangementPossible(
            [possibleSprings[i] if type(i) == int else i for i in springsList],
            damagedGroups)

    return possibleCombinations


print("Total Number of Arrangements:",
    sum([getNumberOfDifferentArrangements(line) for line in INPUT_LINES]))
