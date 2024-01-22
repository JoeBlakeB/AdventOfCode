#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 12: Hot Springs
# Usage:
#     python 2023/12-Hot-Springs.py < 2023/inputs/12.txt

import sys

INPUT_LINES = [line.strip() for line in sys.stdin if line.strip()]


def countPossibleArrangements(springs: list[str], damagedGroups: list[int]) -> int:
    states = "." + ".".join(["#" * group for group in damagedGroups]) + "."

    previousDict = {0: 1}
    nextDict = {}
    for char in springs:
        for stateIndex, count in previousDict.items():
            if char == "?":
                if stateIndex + 1 < len(states):
                    nextDict[stateIndex + 1] = nextDict.get(stateIndex + 1, 0) + count
                if states[stateIndex] == ".":
                    nextDict[stateIndex] = nextDict.get(stateIndex, 0) + count

            elif char == ".":
                if stateIndex + 1 < len(states) and states[stateIndex + 1] == ".":
                    nextDict[stateIndex + 1] = nextDict.get(stateIndex + 1, 0) + count
                if states[stateIndex] == ".":
                    nextDict[stateIndex] = nextDict.get(stateIndex, 0) + count

            elif char == "#":
                if stateIndex + 1 < len(states) and states[stateIndex + 1] == "#":
                    nextDict[stateIndex + 1] = nextDict.get(stateIndex + 1, 0) + count
        
        previousDict = nextDict
        nextDict = {}
    
    return previousDict.get(len(states) - 1, 0) + previousDict.get(len(states) - 2, 0)



beforeUnfolding = 0
afterUnfolding = 0
for line in INPUT_LINES:
    damagedGroups: list[int] = [int(num) for num in line.split()[1].split(",")]
    springsString = line.split()[0]
    beforeUnfolding += countPossibleArrangements(
        springsString, damagedGroups)
    afterUnfolding += countPossibleArrangements(
        "?".join([springsString] * 5), damagedGroups * 5)


print("Total Number of Arrangements:", beforeUnfolding)

print("Total Number of Arrangements After Unfolding:", afterUnfolding)

