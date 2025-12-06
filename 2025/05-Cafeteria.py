#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 5: Cafeteria
# Usage:
#     python 2025/05-Cafeteria.py < 2025/inputs/05.txt

import sys

FRESH_RANGES = [list((int(a), int(b)) for a, b in [r.split("-")])[0] for r in iter(lambda: next(sys.stdin).rstrip("\n"), "")]
INGREDIENTS = [int(i) for i in list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))]
FRESH_INGREDIENTS = [i for i in INGREDIENTS if any([i in range(r[0], r[1]+1) for r in FRESH_RANGES])]
print("amount of fresh ingredients:", len(FRESH_INGREDIENTS))

intervals = [FRESH_RANGES[0]]
for newStart, newEnd in FRESH_RANGES[1:]:
    added = False
    newIntervals = []

    for start, end in intervals:
        if newEnd < start - 1:
            if not added:
                newIntervals.append((newStart, newEnd))
                added = True
            newIntervals.append((start, end))
        elif newStart > end + 1:
            newIntervals.append((start, end))
        else:
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)

    if not added:
        newIntervals.append((newStart, newEnd))

    intervals = newIntervals

print("total unique fresh ingredients:", sum(end - start + 1 for start, end in intervals))