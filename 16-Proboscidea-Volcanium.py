#!/usr/bin/env python3

# Day 16: Proboscidea Volcanium

import re

with open("inputs/16.txt") as f:
    data = f.read().strip().split("\n")

allValves = {}

for valve in data:
    valve = re.findall(r"Valve (\w+) has flow rate=(\d+); tunnels{0,1} leads{0,1} to valves{0,1} (.*)",valve)[0]
    allValves[valve[0]] = {"flowRate": int(valve[1]), "connections": valve[2].split(", ")}

def calculateDistance(start, end):
    queue = [start]
    checked = [start]
    distances = {start: 1}
    while len(queue) > 0:
        valve = queue.pop(0)
        if valve == end:
            return distances[valve]
        for connection in allValves[valve]["connections"]:
            if connection not in checked:
                queue.append(connection)
                checked.append(valve)
            if (connection not in distances or 
                    distances[connection] > distances[valve] + 1):
                distances[connection] = distances[valve] + 1

    raise Exception(f"Could Not Find Path Between Valves {start} and {end}")

valves = {}

for valve in allValves.keys():
    if allValves[valve]["flowRate"] != 0 or valve == "AA":
        valves[valve] = allValves[valve]
        otherValves = {}
        for otherValve in [v for v in allValves.keys() if v != valve]:
            if otherValve != "AA" and allValves[otherValve]["flowRate"] != 0:
                otherValves[otherValve] = calculateDistance(valve, otherValve)
        valves[valve]["otherValves"] = otherValves

def simulateValves(
        currentValve,
        valvesNotOpened,
        currentPressureReleased,
        pressurePerMinute,
        minutesLeft):
    highestPressureReleased = 0
    otherValves = valves[currentValve]["otherValves"]
    if valvesNotOpened == []:
        return currentPressureReleased + (pressurePerMinute * minutesLeft)
    for valve in valvesNotOpened:
        if otherValves[valve] >= minutesLeft:
            pressureReleased = currentPressureReleased + (pressurePerMinute * minutesLeft)
        else:
            pressureReleased = simulateValves(valve,
                [v for v in valvesNotOpened if v != valve],
                currentPressureReleased + (pressurePerMinute * otherValves[valve]),
                pressurePerMinute + valves[valve]["flowRate"],
                minutesLeft - otherValves[valve])
        if pressureReleased > highestPressureReleased:
            highestPressureReleased = pressureReleased
    return highestPressureReleased

print("The most pressure that can be released:",
    simulateValves("AA", 
        [v for v in valves.keys() if v != "AA"],
        0, 0, 30))

# Split the list of valves into pairs of lists
# Then go through each pair and calculate the pressure released
# The elf and elephant can complete their list independently
# Pressure released will then be combined for the total of that pair

def findAllValveCombinations(valves):
    combinations = [[[valves[0]], []]]
    for valve in valves[1:]:
        combinationsLeft = [[[a for a in b] for b in c] for c in combinations]
        combinationsRight = [[[a for a in b] for b in c] for c in combinations]
        for combination in combinationsLeft:
            combination[0].append(valve)
        for combination in combinationsRight:
            combination[1].append(valve)
        combinations = combinationsLeft + combinationsRight

    return combinations

allRoutes = findAllValveCombinations([v for v in valves.keys() if v != "AA"])

highestPressureReleased = 0

for i in range(len(allRoutes)):
    print(f"Calculating with an elephant: {int((i/len(allRoutes))*100)}%", end="\r")
    highestPressureReleased = max(highestPressureReleased, 
        simulateValves("AA", allRoutes[i][0], 0, 0, 26) + simulateValves("AA", allRoutes[i][1], 0, 0, 26))

print("Pressure released with an elephant helping:", highestPressureReleased)
