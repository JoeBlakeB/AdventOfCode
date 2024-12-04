#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 4: Ceres Search
# Usage:
#     python 2024/04-Ceres-Search.py < 2024/inputs/04.txt

import sys

grid = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))

findXMASHorizontal = lambda grid : sum([line.count("XMAS") for line in grid])

def findXMASDiagonal(grid):
    count = 0
    for y in range(len(grid)-3):
        for x in range(len(grid[y])-3):
            word = grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2] + grid[y+3][x+3]
            if word == "XMAS":
                count += 1
    return count


def findX_MAS(grid):
    count = 0
    for y in range(len(grid)-2):
        for x in range(len(grid[y])-2):
            if (
                grid[y][x] == "M" and grid[y][x+2] == "S" and
                        grid[y+1][x+1] == "A" and
                grid[y+2][x] == "M" and grid[y+2][x+2] == "S"
            ):
                count += 1
    return count

xmasCount = 0
crossCount = 0
for i in range(4):
    xmasCount += findXMASHorizontal(grid)
    xmasCount += findXMASDiagonal(grid)
    crossCount += findX_MAS(grid)
    grid = ["".join(row) for row in zip(*grid[::-1])](grid)

print("XMAS Count:", xmasCount)
print("X-MAS Count:", crossCount)
