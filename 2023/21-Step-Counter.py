#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 21: Step Counter
# Usage:
#     python 2023/21-Step-Counter.py < 2023/inputs/21.txt

import sys

GARDEN_MAP = [line.strip() for line in sys.stdin if line.strip()]
HEIGHT = len(GARDEN_MAP)
WIDTH = len(GARDEN_MAP[0])
if not all([len(line) == WIDTH for line in GARDEN_MAP]):
    raise Exception("Not all lines are the same width")
COORDINATE_CHANGES = ((-1, 0), (1, 0), (0, 1), (0, -1))


def getStartPoint() -> tuple[int, int]:
    for y, line in enumerate(GARDEN_MAP):
        if "S" in line:
            return y, line.index("S")
    raise Exception("Could not find start point")


def getReachablePlotsAfterSteps(steps: int, reached: set = None, otherReached: set = None, reachedLastStep: list = None, cannotGoOutside: bool = True
                                ) -> tuple[int, set, set, list]:
    if reached is None or otherReached is None or reachedLastStep is None:
        reached = set([getStartPoint()])
        otherReached = set()
        reachedLastStep = [getStartPoint()]

    for i in range(steps):
        reached, otherReached = otherReached, reached
        reachedThisStep = []
        
        for pos in reachedLastStep:
            for y, x in ((pos[0]+y2, pos[1]+x2) for y2, x2 in COORDINATE_CHANGES):
                if cannotGoOutside and (y < 0 or x < 0 or y >= HEIGHT or x >= WIDTH):
                    continue
                if GARDEN_MAP[y%HEIGHT][x%WIDTH] == "#":
                    continue
                if (y, x) in reached or (y, x) in otherReached:
                    continue
                reached.add((y, x))
                reachedThisStep.append((y, x))
        
        reachedLastStep = reachedThisStep
    
    return len(reached), reached, otherReached, reachedLastStep


def calculateReachablePlotsAfterSteps(steps: int) -> int:
    firstDistance, r, oR, rLS = getReachablePlotsAfterSteps((WIDTH-1)//2, cannotGoOutside=False)
    secondDistance, r, oR, rLS = getReachablePlotsAfterSteps(WIDTH, r, oR, rLS, False)
    thirdDistance = getReachablePlotsAfterSteps(WIDTH, r, oR, rLS, False)[0]

    # Get a, b, and c for the quadratic formula f(n) = an^2 + bn + c
    a = (thirdDistance - (2 * secondDistance) + firstDistance) // 2
    b = secondDistance - firstDistance - a
    c = firstDistance
    n = (steps - ((WIDTH-1)//2)) // WIDTH
    return (a * n**2) + (b * n) + c


print("Plots After 64 Steps:", getReachablePlotsAfterSteps(64)[0])
print("Plots After 26501365 Steps:", calculateReachablePlotsAfterSteps(26501365))
