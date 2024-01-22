#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 11: Cosmic Expansion
# Usage:
#     python 2023/11-Cosmic-Expansion.py < 2023/inputs/11.txt

import itertools
import sys
import typing


def expandUniverse(universe: list[str]) -> list[list[bool]]:
    lineLength = len(universe[0])
    if not all([len(line) == lineLength for line in universe]):
        raise Exception("Not all lines are the same width")

    universeExpansionRows = []
    for i, row in enumerate(universe):
        if "#" not in row:
            universeExpansionRows.append(i)
    
    universeExpansionColumns = []
    for column in range(len(universe[0])):
        for row in range(len(universe)):
            if universe[row][column] == "#":
                break
        else:
            universeExpansionColumns.append(column)
    
    return universe, universeExpansionRows, universeExpansionColumns


UNIVERSE, UNIVERSE_EXPANSION_ROWS, UNIVERSE_EXPANSION_COLUMNS = expandUniverse(
    [line.strip() for line in sys.stdin if line.strip()])


def galaxyGenerator(universe: list[list[bool]]) -> typing.Iterator[tuple[int, int]]:
    for y, row in enumerate(universe):
        for x, galaxy in enumerate(row):
            if galaxy == "#":
                yield y, x


def distanceBetweenUniverses(u1: tuple[int, int], u2: tuple[int, int], expansion: int) -> int:
    topLeft = [min(u1[0], u2[0]), min(u1[1], u2[1])]
    bottomRight = [max(u1[0], u2[0]), max(u1[1], u2[1])]
    extra = 0
    for row in UNIVERSE_EXPANSION_ROWS:
        if topLeft[0] < row < bottomRight[0]:
            extra += expansion
    for column in UNIVERSE_EXPANSION_COLUMNS:
        if topLeft[1] < column < bottomRight[1]:
            extra += expansion
    return abs(u1[0] - u2[0]) + abs(u1[1] - u2[1]) + extra


def sumUniverseExpansion(expansionAmount: int) -> int:
    return sum([distanceBetweenUniverses(u1, u2, expansionAmount) for u1, u2 in itertools.combinations(galaxyGenerator(UNIVERSE), 2)])


print("Sum of Distances Between Universes:", sumUniverseExpansion(1))

print("With a Million Times Expansion:", sumUniverseExpansion(999999))
