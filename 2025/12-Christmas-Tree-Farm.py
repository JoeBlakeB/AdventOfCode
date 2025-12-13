#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 12: Christmas Tree Farm
# Usage:
#     python 2025/12-Christmas-Tree-Farm.py < 2025/inputs/12.txt

import sys

regions = ["#"]
while any("#" in line for line in regions):
    regions = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))

regionSizes = []
regionPresentCounts = []
for region in regions:
    size, gifts = region.split(": ")
    w, h = size.split("x")
    regionSizes.append(int(w) // 3 * int(h) // 3)
    regionPresentCounts.append([int(x) for x in gifts.split(" ")])

print("regions fit unorganised presents i guess?",
      sum(1 if size >= sum(gifts) else 0 for size, gifts in zip(regionSizes, regionPresentCounts)))