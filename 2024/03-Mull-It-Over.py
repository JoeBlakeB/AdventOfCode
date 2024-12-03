#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 3: Mull It Over
# Usage:
#     python 2024/03-Mull-It-Over.py < 2024/inputs/03.txt

import re
import sys
from math import prod

INPUT_LINES = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))

allMulMatches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", "\n".join(INPUT_LINES))
sumMulInstructions = lambda muls : sum([prod(map(int, mul[4:-1].split(","))) for mul in muls])
print("Summed Multiplications:", sumMulInstructions(allMulMatches))

allInstructions = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do(?:n't|)\(\))", "\n".join(INPUT_LINES))
doMulInstructions = []
doEnabled = True
for instruction in allInstructions:
    if instruction == "do()":
        doEnabled = True
    elif instruction == "don't()":
        doEnabled = False
    elif doEnabled:
        doMulInstructions.append(instruction)
print("After Ignoring Disabled Instructions:", sumMulInstructions(doMulInstructions))
