#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 14: Parabolic Reflector Dish
# Usage:
#     python 2023/14-Parabolic-Reflector-Dish.py < 2023/inputs/14.txt

import sys


class TiltDirection:
    # (Rotate Grid, Reverse Lines)
    North = (True, True)
    South = (True, False)
    East = (False, False)
    West = (False, True)

tiltDirections = (TiltDirection.North, TiltDirection.West, TiltDirection.South, TiltDirection.East)


class Platform:
    def __init__(self, rocks: list[str]) -> None:
        self.rocks = rocks

    def __str__(self):
        return "\n".join(self.rocks)
    
    def getRotatedRocks(self) -> list[str]:
        rotated = [""] * len(self.rocks[0])
        for line in self.rocks:
            rotated = [x + y for x, y in zip(rotated, line)]
        return rotated
    
    def __eq__(self, platform: "Platform") -> bool:
        if not isinstance(platform, Platform): return False
        return self.rocks == platform.rocks
    
    def tilt(self, tiltDirection: TiltDirection) -> int:
        if tiltDirection[0]:
            oldRocks = self.getRotatedRocks()
            newRocks = [""] * len(self.rocks)
        else:
            oldRocks = self.rocks
            newRocks = []

        supportBeamLoad = 0
        
        for rowOrColumn in oldRocks:
            if tiltDirection[1]: rowOrColumn = rowOrColumn[::-1]
            rowOrColumn = "#".join(("".join(sorted(group)) for group in rowOrColumn.split("#")))
            supportBeamLoad += sum([i if rock == "O" else 0 for i, rock in enumerate(rowOrColumn, 1)])
            if tiltDirection[1]: rowOrColumn = rowOrColumn[::-1]

            if tiltDirection[0]:
                newRocks = [x + y for x, y in zip(newRocks, rowOrColumn)]
            else:
                newRocks.append(rowOrColumn)
        
        self.rocks = newRocks
        return supportBeamLoad
    
    def getLoadOnSupportBeams(self, tiltDirection: TiltDirection) -> int:
        if tiltDirection[0]:
            rocks = self.getRotatedRocks()
        else:
            rocks = self.rocks

        supportBeamLoad = 0
        
        for rowOrColumn in rocks:
            if tiltDirection[1]: rowOrColumn = rowOrColumn[::-1]
            supportBeamLoad += sum([i if rock == "O" else 0 for i, rock in enumerate(rowOrColumn, 1)])
        
        return supportBeamLoad

    def runSpinCycle(self, cyclesRequired: int):
        rocksSoFar = []

        while self.rocks not in rocksSoFar[:-1]:
            for tiltDirection in tiltDirections:
                self.tilt(tiltDirection)
            rocksSoFar.append(self.rocks)

        cycleStart = rocksSoFar.index(self.rocks) + 1
        cycleLength = len(rocksSoFar) - cycleStart
        cyclesRemaining = (cyclesRequired - cycleStart) % cycleLength

        for i in range(cyclesRemaining):
            for tiltDirection in tiltDirections:
                self.tilt(tiltDirection)


platform = Platform([line.strip() for line in sys.stdin if line.strip()])

print("Total Load on the North Support Beams:", Platform(platform.rocks).tilt(TiltDirection.North))

platform.runSpinCycle(1_000_000_000)

print("Load After 1 Billion Spin Cycles:", platform.getLoadOnSupportBeams(TiltDirection.North))
