#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 10: Factory
# Usage:
#     python 2025/10-Factory.py < 2025/inputs/10.txt

import sys

INPUT = [line.split(" ") for line in iter(lambda: next(sys.stdin).rstrip("\n"), "")]
LIGHTS = [[char == "#" for char in line[0][1:-1]] for line in INPUT]
BUTTONS = [[[int(num) for num in button[1:-1].split(",")] for button in line[1:-1]] for line in INPUT]
POWER = [[int(num) for num in line[-1][1:-1].split(",")] for line in INPUT]

def pressButtonsForLights(lights, buttons) -> int:
    previousLightPatterns = [([False] * len(lights), buttons.copy())]
    timesPressed = 0
    while True:
        nextLightPatterns = []
        timesPressed += 1
        for pattern, allowedButtons in previousLightPatterns:
            for button in allowedButtons:
                newPattern = pattern.copy()
                for change in button:
                    newPattern[change] = not newPattern[change]
                if newPattern == lights:
                    return timesPressed
                newAllowedButtons = allowedButtons.copy()
                newAllowedButtons.remove(button)
                nextLightPatterns.append((newPattern, newAllowedButtons))
        previousLightPatterns = nextLightPatterns
        

print("fewest button presses to turn all machines on:",
      sum(pressButtonsForLights(l, b) for l, b in zip(LIGHTS, BUTTONS)))
