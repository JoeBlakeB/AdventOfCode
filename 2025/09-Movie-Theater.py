#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 9: Movie Theater
# Usage:
#     python 2025/09-Movie-Theater.py < 2025/inputs/09.txt

import sys
from itertools import combinations
from shapely.geometry import Polygon

RED_TILES = [(int(tile.split(",")[0]), int(tile.split(",")[1])) for tile in iter(lambda: next(sys.stdin).rstrip("\n"), "")]
POSSIBLE_RECTANGLES = [(min(a, x), min(b, y), max(a, x), max(b, y))
    for ((a, b), (x, y)) in combinations(RED_TILES, 2)]

print("largest area with any tiles:", max([
    ((x - a + 1) * (y - b + 1)) for a, b, x, y in POSSIBLE_RECTANGLES
]))

polygon = Polygon(RED_TILES)

print("largest area with red and green tiles:", max([
    ((x - a + 1) * (y - b + 1)) for a, b, x, y in POSSIBLE_RECTANGLES
    if polygon.covers(Polygon([(a, b), (x, b), (x, y), (a, y)]))
]))
