#!/usr/bin/env python3

# Advent of Code 2023 - Day 8: Haunted Wasteland
# Usage:
#     python 2023/08-Haunted-Wasteland.py < 2023/inputs/08.txt

import fileinput
from math import lcm

inputSplit = [line.strip() for line in list(fileinput.input())]

INSTRUCTIONS = [(0 if i == "L" else 1) for i in inputSplit[0]]
NETWORK = {node[0]: (node[2][1:4], node[3][:3]) for node in
    [line.split() for line in inputSplit[1:] if line.strip()]}

def howManySteps(fromPosition, toPosition):
    step = 0
    currentPosition = fromPosition
    while not currentPosition.endswith(toPosition):
        leftOrRight = INSTRUCTIONS[step % len(INSTRUCTIONS)]
        currentPosition = NETWORK[currentPosition][leftOrRight]
        step += 1
    return step

def getDistanceToFirst(start: str) -> int:
    step = 0
    currentPosition = start
    while currentPosition[2] != "Z":
        leftOrRight = INSTRUCTIONS[step % len(INSTRUCTIONS)]
        currentPosition = NETWORK[currentPosition][leftOrRight]
        step += 1
    return step

def howManyStepsAllGhosts():
    startingPositions = [n for n in NETWORK if n[2] == "A"]
    allGhostsDistances = [howManySteps(ghost, "Z") for ghost in startingPositions]
    return lcm(*allGhostsDistances)

if "AAA" in NETWORK:
    print("How many steps are required to reach ZZZ:",
          howManySteps("AAA", "ZZZ"))

print("How many steps untill all ghosts get to a **Z node:",
      howManyStepsAllGhosts())
