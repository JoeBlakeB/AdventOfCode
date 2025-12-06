#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 6: Trash Compactor
# Usage:
#     python 2025/06-Trash-Compactor.py < 2025/inputs/06.txt

import sys
import math

doTheMaths = lambda nums, op: sum(nums) if op == "+" else math.prod(nums)

INPUT = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))
HUMAN_WORKSHEET = [[n for n in line.split() if n] for line in INPUT]
HUMAN_PROBLEMS = [([int(n) for n in nums], op) for nums, op in zip(zip(*HUMAN_WORKSHEET[:-1]), HUMAN_WORKSHEET[-1])]
print("human worksheet grand total:", sum([doTheMaths(nums, op) for nums, op in HUMAN_PROBLEMS]))

grandTotal = 0
numbers = []

for column in list(zip(*INPUT))[::-1]:
    currentNumber = 0

    for char in column:
        if char == " ":
            continue
    
        elif char in ["+", "*"]:
            if currentNumber: numbers.append(currentNumber)
            currentNumber = 0
            x = doTheMaths(numbers, char)
            grandTotal += x
            numbers = []

        else:
            currentNumber *= 10
            currentNumber += int(char)
    
    if currentNumber: numbers.append(currentNumber)

print("cephalopod worksheet grand total:", grandTotal)

print("cursed cephalopod oneliner:",
    sum([sum(nums) if op == "+" else math.prod(nums) for nums, op in 
    [([int(n) for n in p[:-1]], p[-1]) for p in [problem.strip().split(" ") for problem in 
    (" ".join(["".join(l).replace(" ", "").replace("+", " +").replace("*", " *")
    if not all(a == " " for a in l) else "-" for l in list(zip(*INPUT))[::-1]]).split("-"))]]]))
