#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 9: Movie Theater
# Usage:
#     python 2025/09-Movie-Theater.py < 2025/inputs/09.txt

import sys
from itertools import combinations

RED_TILES = [(int(tile.split(",")[0]), int(tile.split(",")[1])) for tile in iter(lambda: next(sys.stdin).rstrip("\n"), "")]
POSSIBLE_RECTANGLES = [(min(a, x), min(b, y), max(a, x), max(b, y))
    for ((a, b), (x, y)) in combinations(RED_TILES, 2)]

print("largest area with any tiles:", max([
    ((x - a + 1) * (y - b + 1)) for a, b, x, y in POSSIBLE_RECTANGLES
]))


GREEN_POLYGON = list(zip(RED_TILES, RED_TILES[1:])) + [(RED_TILES[-1], RED_TILES[0])]

def insidePolygon(px: int, py: int):
    for ((x1, y1), (x2, y2)) in GREEN_POLYGON:
        if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
            if (x2 - x1) * (py - y1) == (y2 - y1) * (px - x1):
                return True

    inside = False
    for ((x1, y1), (x2, y2)) in GREEN_POLYGON:
        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

def isLineIntersected(start: tuple[int, int], end: tuple[int, int]):
    (x1, y1), (x2, y2) = start, end
    x1, x2, y1, y2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    horisontal = (y1 == y2)

    for ((x3, y3), (x4, y4)) in GREEN_POLYGON:        
        if horisontal:
            if min(y3, y4) < y1 < max(y3, y4):
                if y3 == y4:
                    continue
                x_cross = x3 + (x4 - x3) * (y1 - y3) / (y4 - y3)
                if x1 < x_cross < x2:
                    return True
        else:
            if min(x3, x4) < x1 < max(x3, x4):
                if x3 == x4:
                    continue
                y_cross = y3 + (y4 - y3) * (x1 - x3) / (x4 - x3)
                if y1 < y_cross < y2:
                    return True

    return False


print("largest area with red and green tiles:", max([
    ((x - a + 1) * (y - b + 1)) for a, b, x, y in POSSIBLE_RECTANGLES
    if not isLineIntersected((a, b), (x, b)) and
       not isLineIntersected((x, b), (x, y)) and
       not isLineIntersected((x, y), (a, y)) and
       not isLineIntersected((a, y), (a, b)) and
        insidePolygon(a + 1, b + 1) and
        insidePolygon(a, b) and 
        insidePolygon(x, y) and 
        insidePolygon(a, y) and 
        insidePolygon(x, b)
]))


from shapely import Polygon
polygon = Polygon(RED_TILES)
print("original library solution that felt too cheaty:", max([
    ((x - a + 1) * (y - b + 1)) for a, b, x, y in POSSIBLE_RECTANGLES
    if polygon.covers(Polygon([(a, b), (x, b), (x, y), (a, y)]))
]))
