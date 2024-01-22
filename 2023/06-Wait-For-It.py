#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 6: Wait For It
# Usage:
#     python 2023/06-Wait-For-It.py < 2023/inputs/06.txt

import fileinput
from operator import mul
from functools import reduce

inputSplit = [line.strip() for line in list(fileinput.input())]
timeDistancePairs = [(int(a), int(b)) for a, b in list(zip(inputSplit[0].split(), inputSplit[1].split()))[1:]]

def getNumberOfPossibleWaysToBeatRecord(maxTime: int, currentRecord: int) -> int:
    for i in range(1, maxTime):
        for timeWaited in range(1, maxTime):
            timeRemaining = maxTime - timeWaited
            if timeRemaining * timeWaited > currentRecord:
                return timeRemaining - timeWaited + 1
    raise Exception("No possible ways to beat record")

print("Product of total ways to beat record:", 
    reduce(mul, (getNumberOfPossibleWaysToBeatRecord(maxTime, currentRecord) for maxTime, currentRecord in timeDistancePairs)))

maxTime, currentRecord = (int("".join(line.split()).split(":")[-1]) for line in inputSplit[:2])

print("Number of total ways to beat record:", getNumberOfPossibleWaysToBeatRecord(maxTime, currentRecord))
      
