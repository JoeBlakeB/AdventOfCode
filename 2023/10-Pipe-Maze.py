#!/usr/bin/env python3

# Advent of Code 2023 - Day 10: Pipe Maze
# Usage:
#     python 2023/10-Pipe-Maze.py < 2023/inputs/10.txt
# Args:
#     --showMap    Shows the part 1 map with distances
#     --showGaps   Shows the part 2 map for gaps in pipes

import sys

PIPES = {
    "|": (True, False, True, False),
    "-": (False, True, False, True),
    "L": (True, True, False, False),
    "J": (True, False, False, True),
    "7": (False, False, True, True),
    "F": (False, True, True, False),
    ".": (False, False, False, False),
    "S": (True, True, True, True)
}
"""pipeChar: (up, right, down, left)"""

DIRECTIONS = (
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
)

MAP = [line.strip() for line in sys.stdin if line.strip()]
HEIGHT = len(MAP)
WIDTH = len(MAP[0])
if not all([len(line) == WIDTH for line in MAP]):
    raise Exception("Not all lines are the same width")


def getStartPoint() -> tuple[int, int]:
    for y, line in enumerate(MAP):
        if "S" in line:
            return y, line.index("S")
    raise Exception("Could not find start point")


def getDistanceToFurthestPoint() -> int:
    alreadyVisited = [[False] * WIDTH for i in range(HEIGHT)]
    visitQueue: list[tuple[int, int, int]] = [(*getStartPoint(), 0)]
    highestDistance = 0

    while visitQueue:
        y, x, distance = visitQueue.pop(0)
        highestDistance = max(highestDistance, distance)
        if alreadyVisited[y][x]:
            continue
        alreadyVisited[y][x] = (distance if distance else "S") if "--showMap" in sys.argv else True
        char = MAP[y][x]
        directions = [(i, a) for i, (a, b) in enumerate(zip(DIRECTIONS, PIPES[char])) if b]

        for i, (yIncrease, xIncrease) in directions:
            y2, x2 = y + yIncrease, x + xIncrease
            if y2 < 0 or x2 < 0 or y2 >= HEIGHT or x2 >= WIDTH or alreadyVisited[y2][x2]:
                continue
            
            otherChar = MAP[y2][x2]
            otherConnects = PIPES[otherChar][(i+2)%4]
            if otherConnects:
                visitQueue.append((y2, x2, distance+1))
    
    if "--showMap" in sys.argv:
        strSize = len(str(highestDistance))
        print("\n".join(
            ["".join([str(c).ljust(strSize) if c else "."*strSize for c in line]) for line in alreadyVisited]
        ), "\n")
    
    return highestDistance


def getMainPipeGridWithSubTiles() -> list[list[bool]]:
    alreadyVisited = [[False] * ((WIDTH*2)-1) for i in range((HEIGHT*2)-1)]
    y, x = getStartPoint()
    alreadyVisited[y*2][x*2] = "#"
    visitQueue: list[tuple[int, int]] = [(y*2, x*2)]

    while visitQueue:
        y, x = visitQueue.pop(0)
        char = MAP[y//2][x//2]
        directions = [(i, a) for i, (a, b) in enumerate(zip(DIRECTIONS, PIPES[char])) if b]

        for i, (yIncrease, xIncrease) in directions:
            y2, x2 = y + (yIncrease*2), x + (xIncrease*2)
            if y2 < 0 or x2 < 0 or y2 >= HEIGHT*2 or x2 >= WIDTH*2:
                continue
            if alreadyVisited[y2][x2]:
                alreadyVisited[y+yIncrease][x+xIncrease] = "0"
                continue

            otherChar = MAP[y2//2][x2//2]
            otherConnects = PIPES[otherChar][(i+2)%4]

            if otherConnects:
                alreadyVisited[y+yIncrease][x+xIncrease] = "x"
                alreadyVisited[y2][x2] = "#"
                visitQueue.append((y2, x2))

    if "--showGaps" in sys.argv:
        print("\n".join(
            ["".join(["#" if c else "." for c in line]) for line in alreadyVisited]
        ), "\n")
    
    return alreadyVisited


def searchFromPoint(tiles, y, x) -> int:
    foundTiles = 0
    visitQueue: list[tuple[int, int]] = [(y, x)]
    outside = False

    while visitQueue:
        y, x = visitQueue.pop(0)
        if y < 0 or x < 0 or y+1 >= HEIGHT*2 or x+1 >= WIDTH*2:
            outside = True
            continue
        if tiles[y][x]:
            continue
        if y % 2 == 0 and x % 2 == 0:
            foundTiles += 1
        tiles[y][x] = True
        
        for yIncrease, xIncrease in DIRECTIONS:
            y2, x2 = y + yIncrease, x + xIncrease
            visitQueue.append((y2, x2))

    return foundTiles * (not outside)


def getEnclosedTilesCount() -> int:
    tiles = getMainPipeGridWithSubTiles()
    foundInsideTiles = 0
    for y in range((HEIGHT*2)-1):
        for x in range((WIDTH*2)-1):
            if tiles[y][x]:
                continue
            else:
                foundInsideTiles += searchFromPoint(tiles, y, x)
    return foundInsideTiles


print("Distance to furthest point:", getDistanceToFurthestPoint())
print("Enclosed Tiles Count:", getEnclosedTilesCount())
