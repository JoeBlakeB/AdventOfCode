#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 3: Gear Ratios
# Usage:
#     python 2023/03-Gear-Ratios.py < 2023/inputs/03.txt

import fileinput
inputSplit = [line.strip() for line in list(fileinput.input())]

def getNumbers(inputSplit: list[str]) -> tuple[list[int], list[int]]:
    adjacentNumbersSum = 0
    gearsSum = 0
    nextToStars = {}
    for y, line in enumerate(inputSplit):
        currentNum = 0
        currentNumSize = 1

        for x, char in enumerate(line):
            if char.isdigit():
                currentNum = currentNum * 10 + int(char)
                currentNumSize += 1
            
            if currentNum and (not char.isdigit() or x == len(line) - 1):
                symbol = symbolInRange(inputSplit,
                                   range(x - currentNumSize, x + 1),
                                   range(y - 1, y + 2))
                
                if symbol[0]:
                    adjacentNumbersSum += currentNum

                    symbolX, symbolY, symbolChar = symbol[1:]
                    if symbolChar == "*":
                        otherNum = nextToStars.pop((symbolX, symbolY), None)
                        if otherNum:
                            gearsSum += currentNum * otherNum
                        else:
                            nextToStars[(symbolX, symbolY)] = currentNum

                currentNum = 0
                currentNumSize = 1
    
    return adjacentNumbersSum, gearsSum


def symbolInRange(inputSplit: list[str], xRange: range, yRange: range
                    ) -> tuple[bool, int|None, int|None, str|None]:
    for y in yRange:
        if y < 0 or y >= len(inputSplit):
            continue
        for x in xRange:
            if x < 0 or x >= len(inputSplit[y]):
                continue
            if inputSplit[y][x] != "." and not inputSplit[y][x].isdigit():
                return True, x, y, inputSplit[y][x]
    return False, None, None, None


adjacentNumbersSum, gearsSum = getNumbers(inputSplit)

print("Sum of adjacent numbers:", adjacentNumbersSum)
print("Sum of gears:", gearsSum)
