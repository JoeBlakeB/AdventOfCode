#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 25: Snowverload
# Usage:
#     python 2023/25-Snowverload.py < 2023/inputs/25.txt

import random
import sys


RANDOM_SAMPLE_COUNT = 100 # just a high enough number that the connections to cut are crossed often enough


def getAllConnections(wireConnectionParts: dict[str, list[str]]) -> dict[str, list[str]]:
    wireConnections = {}
    for left, rights in wireConnectionParts.items():
        wireConnections[left] = wireConnections.get(left, []) + rights
        for right in rights:
            wireConnections[right] = wireConnections.get(right, []) + [left]
    return wireConnections


def getShortestRoute(start, end) -> list[str]:
    queue = [[start]]
    visited = []
    while queue:
        currentRoute = queue.pop(0)
        if end == currentRoute[-1]:
            return currentRoute
        visited.append(currentRoute[-1])
        for component in ALL_WIRE_CONNECTIONS[currentRoute[-1]]:
            if component not in visited and component not in queue:
                queue.append(currentRoute + [component])
    raise Exception


def getThreeMostCommonConnections() -> tuple[tuple[str]]:
    connectionUses: dict[tuple[str], int] = {}
    for i in range(RANDOM_SAMPLE_COUNT):
        start, end = random.choice(list(ALL_WIRE_CONNECTIONS.keys())), random.choice(list(ALL_WIRE_CONNECTIONS.keys()))
        if start == end: continue
        route = getShortestRoute(start, end)
        for i in range(1, len(route)):
            a, b = route[i-1], route[i]
            a, b = min(a, b), max(a, b)
            connectionUses[(a, b)] = connectionUses.get((a, b), 0) + 1

    connectionUsesSorted = sorted([(count, pair) for pair, count in connectionUses.items()])
    return [b for a, b in connectionUsesSorted[-3:]]


def countNumberOfConnectedNodes(start, cutConnections) -> int:
    queue = [start]
    visited = []
    while queue:
        current = queue.pop(0)
        visited.append(current)
        for component in ALL_WIRE_CONNECTIONS[current]:
            if (
                component not in visited and component not in queue
                and not (current, component) in cutConnections
                and not (component, current) in cutConnections
            ):
                queue.append(component)
    return len(visited)


WIRE_CONNECTIONS = {l: r.split() for l, r in [line.strip().split(": ") for line in sys.stdin if line.strip()]}
ALL_WIRE_CONNECTIONS = getAllConnections(WIRE_CONNECTIONS)

connectionsToCut = getThreeMostCommonConnections()
groupOneCount = countNumberOfConnectedNodes(connectionsToCut[0][0], connectionsToCut)
groupTwoCount = len(ALL_WIRE_CONNECTIONS) - groupOneCount

print("Seperated Group Sizes Multiplied Together:", groupOneCount * groupTwoCount)

