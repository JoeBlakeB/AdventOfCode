#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 18: Boiling Boulders

with open("inputs/18.txt") as f:
    data = f.read().strip().split("\n")
    data = [([int(x) for x in line.split(",")]) for line in data]

maxSize = 1 + max([max(x) for x in data])

grid = [[[0 for i in range(maxSize)] for i in range(maxSize)]
        for i in range(maxSize)]

for x, y, z in data:
    grid[x][y][z] = 1

directions = (
    lambda x, y, z: (x + 1, y, z),
    lambda x, y, z: (x - 1, y, z),
    lambda x, y, z: (x, y + 1, z),
    lambda x, y, z: (x, y - 1, z),
    lambda x, y, z: (x, y, z + 1),
    lambda x, y, z: (x, y, z - 1))

isExternalCache = {}

def isExternal(x, y, z, checked=[]):
    if (x, y, z) in isExternalCache:
        return isExternalCache[(x, y, z)]
    checked = checked + [[x, y, z]]
    for direction in directions:
        x2, y2, z2 = direction(x, y, z)
        if [x2, y2, z2] in checked:
            continue
        if (x2 < 0 or x2 >= maxSize or
            y2 < 0 or y2 >= maxSize or
                z2 < 0 or z2 >= maxSize):
            isExternalCache[(x, y, z)] = True
            return True
        elif grid[x2][y2][z2] == 1:
            continue
        if isExternal(x2, y2, z2, checked):
            isExternalCache[(x, y, z)] = True
            return True
    isExternalCache[(x, y, z)] = False
    return False

totalArea = 0
exteriorArea = 0
for x, y, z in data:
    for direction in directions:
        x2, y2, z2 = direction(x, y, z)
        if (x2 < 0 or x2 >= maxSize or
            y2 < 0 or y2 >= maxSize or
                z2 < 0 or z2 >= maxSize):
            totalArea += 1
            exteriorArea += 1
        elif grid[x2][y2][z2] != 1:
            totalArea += 1
            if isExternal(x2, y2, z2):
                exteriorArea += 1
                
# print("\n\n".join(["\n".join(["".join(["░█xo#"[x] for x in y]) for y in z]) for z in grid]))

print("Surface area of scanned lava droplet:", totalArea)
print("Exterior surface area of scanned lava droplet:", exteriorArea)