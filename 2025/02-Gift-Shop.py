#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 2: Gift Shop
# Usage:
#     python 2025/02-Gift-Shop.py < 2025/inputs/02.txt

import sys

ID_RANGES = [[int(n) for n in r.split("-")]
             for r in "\n".join(list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))).split(",")]

def invalidValidNumber1(id: str):
    if len(id) % 2 != 0: return False
    return id[: len(id)//2] == id[len(id)//2 :]

def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def invalidValidNumber2(id: str):
    for divisor in divisors(len(id))[1:]:
        if invalidValidNumberAtSplitLength(id, divisor) == True:
            return True
    return False

def invalidValidNumberAtSplitLength(id: str, numSplits: int):
    if len(id) % numSplits != 0: return False

    segLen = len(id)//numSplits
    segments = [id[: segLen], id[segLen * (numSplits-1) :]]
    for s in range(1, numSplits-1):
        segments.append(id[segLen * s : segLen * (s+1)])

    for seg in segments[1:]:
        if seg != segments[0]:
            return False
    return True

invalidNumberSum1 = 0
invalidNumberSum2 = 0

for a, b in ID_RANGES:
    for i in range(a, b+1):
        strI = str(i)
        if invalidValidNumber1(strI):
            invalidNumberSum1 += i
        if invalidValidNumber2(strI):
            invalidNumberSum2 += i

print("single split invalid IDs:", invalidNumberSum1)
print("any count split invalid IDs:", invalidNumberSum2)
