#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 7: Bridge Repair
# Usage:
#     python 2024/07-Bridge-Repair.py < 2024/inputs/07.txt

import sys

EQUATIONS = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))

def isCalculationPossible(final, values):
    if len(values) == 2:
        return (values[0] + values[1] == final or
                values[0] * values[1] == final)
    else:
        return (
            isCalculationPossible(final, [values[0] + values[1], *values[2:]]) or
            isCalculationPossible(final, [values[0] * values[1], *values[2:]]))

def isCalculationPossibleWithConcatenation(final, values):
    if len(values) == 2:
        return (values[0] + values[1] == final or
                values[0] * values[1] == final or
                int(f"{values[0]}{values[1]}") == final)
    else:
        return (
            isCalculationPossibleWithConcatenation(final, [values[0] + values[1], *values[2:]]) or
            isCalculationPossibleWithConcatenation(final, [values[0] * values[1], *values[2:]]) or
            isCalculationPossibleWithConcatenation(final, [int(f"{values[0]}{values[1]}"), *values[2:]]))

calibrationResult = 0
calibrationResultWithConcatenation = 0
for equations in EQUATIONS:
    final, values = equations.split(": ")
    final = int(final)
    values = [int(v) for v in values.split()]

    if isCalculationPossible(final, values):
        calibrationResult += final

    if isCalculationPossibleWithConcatenation(final, values):
        calibrationResultWithConcatenation += final

print("Total Calibration Result:", calibrationResult)
print("      with Concatenation:", calibrationResultWithConcatenation)
