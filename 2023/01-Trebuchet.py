#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 1: Trebuchet?!
# Usage:
#     python 2023/01-Trebuchet.py < 2023/inputs/01.txt

import fileinput
inputSplit = list(fileinput.input())

digitWordList = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def replaceFirstDigit(line, reverse=False):
    if reverse:
        wordList = {word[::-1]: digitWordList[word] for word in digitWordList}
    else:
        wordList = digitWordList
    
    for start in range(len(line) - 1):
        for end in range(start, len(line)+1):
            if line[start:end] in wordList:
                line = line[:start] + wordList[line[start:end]] + line[end:]
    return line

def sumDigitsOnLine(inputSplit, partTwo):
    total = 0

    for line in inputSplit:
        firstNum = 0
        lastNum = 0

        lineRev = line[::-1]

        if partTwo:
            line = replaceFirstDigit(line)
            lineRev = replaceFirstDigit(lineRev, reverse=True)

        firstNum = next(int(char) for char in line if char.isdigit())
        lastNum = next(int(char) for char in lineRev if char.isdigit())

        total += firstNum * 10 + lastNum

    return total

print("Part 1:", sumDigitsOnLine(inputSplit, partTwo=False))
print("Part 2:", sumDigitsOnLine(inputSplit, partTwo=True))
