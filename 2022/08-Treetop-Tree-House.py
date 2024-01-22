#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 8: Treetop Tree House

with open("inputs/08.txt") as f:
    data = f.read().strip().split("\n")

# Get the map as arrays
gridSize = len(data)
map = []
for row in data:
    map.append(list(row))
counted = []
for i in range(len(map)):
    counted.append([" "] * gridSize)

# Trees visible from outside of the forest

getCoordinates1 = {
    "n": lambda x, y: (y, x),
    "e": lambda x, y: (x, gridSize - y - 1),
    "s": lambda x, y: (gridSize - y - 1, gridSize - x - 1),
    "w": lambda x, y: (gridSize - x - 1, y)
}

trees = 0
for direction in ("n", "e", "s", "w"):
    for a in range(gridSize):
        treeMaxHeight = -1
        for b in range(gridSize):
            x, y = getCoordinates1[direction](a, b)
            height = int(map[x][y])
            if height > treeMaxHeight:
                treeMaxHeight = height
                if counted[x][y] == " ":
                    trees += 1
                    counted[x][y] = "X"

print("Trees counted from outside:", trees)

# Trees visible from inside the forest

getDistanceToEdge = {
    "n": lambda x, y: x + 1,
    "e": lambda x, y: gridSize - y,
    "s": lambda x, y: gridSize - x,
    "w": lambda x, y: y + 1
}

getCoordinates2 = {
    "n": lambda x, y, i: (x-i, y),
    "e": lambda x, y, i: (x, y+i),
    "s": lambda x, y, i: (x+i, y),
    "w": lambda x, y, i: (x, y-i)
}

highestScenicScore = 0

for x in range(gridSize):
    for y in range(gridSize):
        currentHeight = int(map[x][y])
        scenicScore = 1
        for lookDirection in ("n", "e", "s", "w"):
            i = 0
            for i in range(1, getDistanceToEdge[lookDirection](x, y)):
                checkX, checkY = getCoordinates2[lookDirection](x, y, i)
                checkHeight = int(map[checkX][checkY])
                if checkHeight >= currentHeight:
                    break
            scenicScore *= i
        if scenicScore > highestScenicScore:
            highestScenicScore = scenicScore

print("Highest scenic score:", highestScenicScore)
