#!/usr/bin/env python3

# Day 14: Regolith Reservoir

with open("inputs/14.txt") as f:
    data = f.read().strip()

class Grid:
    horisontalMin = 500
    horisontalMax = 500
    verticalSize = 0
    gridWidth = 1
    grid = [[0]]

    def __init__(self, grid=None):
        if grid:
            self.horisontalMin = grid.horisontalMin
            self.horisontalMax = grid.horisontalMax
            self.verticalSize = grid.verticalSize
            self.gridWidth = grid.gridWidth
            self.grid = [row[:] for row in grid.grid]

    def __str__(self):
        return "\n".join(["".join(" █░x-"[i] for i in row) for row in self.grid])

    def __repr__(self):
        return self.__str__()

    def addLocation(self, key, value=1):
        if key[0] < self.horisontalMin:
            self.addHorisontalPadding(key[0], "left")
        if key[0] > self.horisontalMax:
            self.addHorisontalPadding(key[0], "right")
        if key[1] > self.verticalSize:
            self.addVerticalPadding(key[1])
        y, x = self.gridPosition(key)
        self.grid[y][x] = value

    def __getitem__(self, key):
        if key[0] < self.horisontalMin or key[0] > self.horisontalMax or key[1] > self.verticalSize:
            return None
        y, x = self.gridPosition(key)
        return self.grid[y][x]

    def addHorisontalPadding(self, size, side):
        if side == "left":
            for i in range(len(self.grid)):
                self.grid[i] = [0] * (self.horisontalMin - size) + self.grid[i]
            self.horisontalMin = size
        else:
            for i in range(len(self.grid)):
                self.grid[i] += [0] * (size - self.horisontalMax)
            self.horisontalMax = size
        self.gridWidth = self.horisontalMax - self.horisontalMin + 1
    
    def addVerticalPadding(self, size):
        for i in range(size - self.verticalSize):
            self.grid.append([0] * self.gridWidth)
        self.verticalSize = size

    def gridPosition(self, position):
        return position[1], position[0] - self.horisontalMin

def parseLine(line):
    locations = line.split(" -> ")
    for i in range(len(locations)):
        x, y = locations[i].split(",")
        locations[i] = (int(x), int(y))
    return locations

grid = Grid()

for line in data.splitlines():
    locations = parseLine(line)
    grid.addLocation(locations[0])
    for i in range(1, len(locations)):
        for j in range(*sorted([1, locations[i][1] - locations[i-1][1]])):
            grid.addLocation((locations[i][0], locations[i-1][1] + j))
        for j in range(*sorted([1, locations[i][0] - locations[i-1][0]])):
            grid.addLocation((locations[i-1][0] + j, locations[i][1]))

grid2 = Grid(grid)

sandCount = 0
while True:
    sandDepth = 1
    sandHorizontal = 500
    while (sandDepth < grid.verticalSize and
            sandHorizontal <= grid.horisontalMax and
            sandHorizontal >= grid.horisontalMin):
        for i in (0, -1, 1):
            if not grid[sandHorizontal + i, sandDepth + 1]:
                sandHorizontal += i
                sandDepth += 1
                break
        else:
            sandCount += 1
            grid.addLocation((sandHorizontal, sandDepth), 2)
            break
    else:
        break

print("Units of sand before reaching the abyss:", sandCount)

sandCount = 0
floorDepth = grid2.verticalSize + 1
while not grid2[500, 0]:
    sandDepth = 0
    sandHorizontal = 500
    sandFalling = True
    while sandDepth < floorDepth and sandFalling:
        for i in (0, -1, 1):
            if not grid2[sandHorizontal + i, sandDepth + 1]:
                sandHorizontal += i
                sandDepth += 1
                break
        else:
            sandFalling = False
    else:
        sandCount += 1
        grid2.addLocation((sandHorizontal, sandDepth), 2)

print("Total units of sand until complete stack:", sandCount)