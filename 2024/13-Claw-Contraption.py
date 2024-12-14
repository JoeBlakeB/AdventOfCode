#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 13: Claw Contraption
# Usage:
#     python 2024/13-Claw-Contraption.py < 2024/inputs/13.txt

import re
import sys

def getCostForPrize(aX, aY, bX, bY, pX, pY):
    aRatio = aX / aY
    bRatio = bX / bY
    aCost, bCost = 3, 1

    if aRatio > bRatio:
        aCost, bCost = bCost, aCost
        aX, aY, bX, bY = bX, bY, aX, aY
        aRatio, bRatio = bRatio, aRatio

    if (pX / pY) < aRatio or (pX / pY) > bRatio:
        return None
    
    minAClicks = 0
    maxAClicks = min(pX // aX, pY // aY) + 1

    while minAClicks < maxAClicks:
        aClicks = (minAClicks + maxAClicks) // 2
        clawX, clawY = aX * aClicks, aY * aClicks
        ratio = ((pX - clawX)) / (pY - clawY)
        if ratio == bRatio:
            bClicks = ((pX - clawX) // bX)
            if (aClicks * aX) + (bClicks * bX) == pX and (aClicks * aY) + (bClicks * bY) == pY:
                return (aClicks * aCost) + (bClicks * bCost)
            else:
                return
        elif ratio > bRatio:
            maxAClicks = aClicks
        else:
            minAClicks = aClicks + 1

totalCost1 = 0
totalCost2 = 0

while True:
    inputSection = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))
    if not inputSection: break

    aX, aY = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", inputSection[0])[0]
    bX, bY = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", inputSection[1])[0]
    pX, pY = re.findall(r"Prize: X=(\d+), Y=(\d+)", inputSection[2])[0]

    cost1 = getCostForPrize(int(aX), int(aY), int(bX), int(bY), int(pX), int(pY))
    cost2 = getCostForPrize(int(aX), int(aY), int(bX), int(bY), int(pX)+10000000000000, int(pY)+10000000000000)

    if cost1 is not None:
        totalCost1 += cost1
    if cost2 is not None:
        totalCost2 += cost2

print("Part 1:", totalCost1)
print("Part 2:", totalCost2)
