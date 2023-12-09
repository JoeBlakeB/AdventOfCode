#!/usr/bin/env python3

# Advent of Code 2023 - Day 9: Mirage Maintenance
# Usage:
#     python 2023/09-Mirage-Maintenance.py < 2023/inputs/09.txt

import fileinput

def predictNextValue(valueHistory: list[int]) -> int:
    allDiffs = [valueHistory]
    while any([value != 0 for value in allDiffs[-1]]):
        diffs = []
        for i in range(len(allDiffs[-1]) - 1):
            thisVal, nextVal = allDiffs[-1][i:i+2]
            diffs.append(nextVal - thisVal)
        allDiffs.append(diffs)

    for i in range(len(allDiffs)-2, -1, -1):
        allDiffs[i].append(allDiffs[i][-1] + allDiffs[i+1][-1])

    return allDiffs[0][-1]
    

oasisReports = [[int(num) for num in line.strip().split()]
                for line in list(fileinput.input()) if line.strip()]

print("Sum of all predicted next values:",
      sum([predictNextValue(report) for report in oasisReports]))

print("Sum of all predicted previous values:",
      sum([predictNextValue(report[::-1]) for report in oasisReports]))
