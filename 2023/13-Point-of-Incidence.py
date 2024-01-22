#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 13: Point of Incidence
# Usage:
#     python 2023/13-Point-of-Incidence.py < 2023/inputs/13.txt

import sys

PATTERNS = [pattern.strip().split("\n") for pattern in 
            sys.stdin.read().split("\n\n") if "\n" in pattern.strip()]

def rotatePattern(pattern: list[str]) -> list[str]:
    output = [""] * len(pattern[0])
    for line in pattern:
        output = [x + y for x, y in zip(output, line)]
    return output


def getReflection(pattern: list[str]) -> int:
    for i in range(len(pattern) - 1):
        for j in range(i+1):
            if i + j + 2 > len(pattern):
                return i + 1
            elif pattern[i-j] != pattern[i+j+1]:
                break
        else:
            return i + 1
    return 0


def getReflectionAllowOneSmudge(pattern: list[str]) -> int:
    for i in range(len(pattern) - 1):
        foundSmudge = False
        for j in range(i+1):
            if i + j + 2 > len(pattern):
                if foundSmudge:
                    return i + 1
                else:
                    break
            elif pattern[i-j] != pattern[i+j+1]:
                if foundSmudge:
                    break
                else:
                    lineA, lineB =  pattern[i-j], pattern[i+j+1]
                    differences = sum([1 for a, b in zip(lineA, lineB) if a != b])
                    if differences == 1:
                        foundSmudge = True
                    else:
                        break
        else:
            if foundSmudge:
                return i + 1
    return 0


print("Pattern Notes Summary:", sum(
    ((100 * getReflection(pattern)) + getReflection(rotatePattern(pattern))
     for pattern in PATTERNS)))

print("Pattern Notes Summary:", sum(
    ((100 * getReflectionAllowOneSmudge(pattern)) + getReflectionAllowOneSmudge(rotatePattern(pattern))
     for pattern in PATTERNS)))
