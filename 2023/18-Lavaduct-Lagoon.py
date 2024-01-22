#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 18: Lavaduct Lagoon
# Usage:
#     python 2023/18-Lavaduct-Lagoon.py < 2023/inputs/18.txt

import sys


def parseDigPlans(lines: list[str]) -> tuple[list[tuple[int]]]:
    lettersNumbersDigPlan = []
    colourDigPlan = []

    getVector = lambda distance, direction: (
        (distance, 0),
        (0, distance),
        (-distance, 0),
        (0, -distance)
    )[direction]

    for line in lines:
        direction, distance, colour = line.split()
        lettersNumbersDigPlan.append(getVector(int(distance), "RDLU".index(direction)))
        colourDigPlan.append(getVector(int(colour[2:-2], 16), int(colour[-2])))

    return lettersNumbersDigPlan, colourDigPlan


def calculateAreaShoelaceTheorem(digPlan: list[tuple[int]]) -> int:
    x, y = digPlan[0]
    areaAndPermiter = abs(x + y)
    
    for i in range(1, len(digPlan)):
        xChange, yChange = digPlan[i]

        x2, y2 = x + xChange, y + yChange
        areaAndPermiter += (x * y2 - y * x2) + abs(x2 - x + y2 - y)

        x, y = x2, y2
    
    return areaAndPermiter // 2 + 1


INPUT_LINES = [line.strip() for line in sys.stdin if line.strip()]
LETTERS_NUMBERS_DIG_PLAN, COLOUR_DIG_PLAN = parseDigPlans(INPUT_LINES)

print("Small Lagoon Lava Capacity:", calculateAreaShoelaceTheorem(LETTERS_NUMBERS_DIG_PLAN))
print("Big Lagoon Lava Capacity:", calculateAreaShoelaceTheorem(COLOUR_DIG_PLAN))
