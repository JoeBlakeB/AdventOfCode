#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 12: Hill Climbing Algorithm

with open("inputs/12.txt") as f:
    data = f.read().strip()
    dataRaw = data.replace("\n", "")

grid = []
for line in data.split("\n"):
    grid.append([{
        "height": "SabcdefghijklmnopqrstuvwxyzE".index(h),
        "pathDistance": -1,
        "distanceLeft": None,
        "path": None,
        "priority": None,
        } for h in line])

height = len(grid)
width = len(grid[0])
priorityQueue = []

def addToPriorityQueue(coordinates):
    location = grid[coordinates[0]][coordinates[1]]
    oldPriority = location["priority"]
    location["priority"] = location["pathDistance"] + location["distanceLeft"]
    if [oldPriority, coordinates] in priorityQueue:
        priorityQueue.remove([oldPriority, coordinates])
    item = [location["priority"], coordinates]
    for i in range(len(priorityQueue)):
        if item[0] < priorityQueue[i][0]:
            return priorityQueue.insert(i, item)
    priorityQueue.append(item)

start = dataRaw.index("S")
start = [start // width, start % width]
end = dataRaw.index("E")
end = [end // width, end % width]

def findPath(start, end):
    grid[start[0]][start[1]]["height"] = 1
    grid[end[0]][end[1]]["height"] = 26

    grid[start[0]][start[1]]["pathDistance"] = 0
    for y in range(height):
        for x in range(width):
            grid[y][x]["distanceLeft"] = abs(end[0] - y) + abs(end[1] - x)

    grid[start[0]][start[1]]["pathDistance"] = 0
    addToPriorityQueue(start)

    while len(priorityQueue) > 0:
        y, x = priorityQueue.pop(0)[1]
        if [y, x] == end:
            break
        location = grid[y][x]
        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            y2, x2 = y + i[0], x + i[1]
            if y2 < 0 or y2 >= height or x2 < 0 or x2 >= width:
                continue
            location2 = grid[y2][x2]
            if location2["height"] > location["height"] + 1:
                continue
            if location2["pathDistance"] > location["pathDistance"] + 1 or location2["pathDistance"] == -1:
                location2["pathDistance"] = location["pathDistance"] + 1
                location2["path"] = [y, x]
                addToPriorityQueue([y2, x2])
    return grid[end[0]][end[1]]["pathDistance"]

def showGrid():
    map = ["\033[1;31m" + char for char in data]
    lastPath = grid[end[0]][end[1]]["path"]
    while lastPath != start:
        y, x = lastPath
        map[y * (width + 1) + x] = "\033[1;32m" + map[y * (width + 1) + x][-1]
        lastPath = grid[y][x]["path"]
    print("".join(map)
        .replace("\033[1;31ma", "\033[1;30ma")
        .replace("\033[1;31mS", "\033[1;34mS")
        .replace("\033[1;31mE", "\033[1;34mE"),
        "\033[1;0m")

shortestPath = findPath(start, end)
showGrid()
print("Number of steps till best signal:", shortestPath)

for i in range(height):
    newStartingLength = findPath([i, 0], end)
    if newStartingLength < shortestPath:
        shortestPath = newStartingLength
print("Fewest number of steps with starting elevation of a:", shortestPath)