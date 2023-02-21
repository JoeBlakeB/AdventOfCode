#!/usr/bin/env python3

# Day 15: Beacon Exclusion Zone

filename = "inputs/15.txt"
with open(filename) as f:
    data = f.read().strip().split("\n")
    sensors = []
    beacons = []
    for line in data:
        sensor, beacon = [[int(pos.split("=")[1]) for pos in coords.split(", ")]
                            for coords in line.split(":")]
        sensors.append([sensor, beacon])
        beacons.append(beacon)

rowForChecking = [2000000, 10]["demo" in filename]
sensorAreas = []
exclusionZones = []
for sensor in sensors:
    beaconDistance = abs(sensor[0][0] - sensor[1][0]) + abs(sensor[0][1] - sensor[1][1])
    sensorAreas.append((sensor[0], beaconDistance))
    if rowForChecking in range(sensor[0][1] - beaconDistance, sensor[0][1] + beaconDistance + 1):
        exclusionZone = beaconDistance - abs(sensor[0][1] - rowForChecking)
        exclusionZones.append((range(sensor[0][0] - exclusionZone, sensor[0][0] + exclusionZone + 1)))

exclusionZone = []
for zone in exclusionZones:
    exclusionZone += [*zone]
noBeaconsOnRow = list(set(exclusionZone))

for beacon in [beacon[0] for beacon in beacons if beacon[1] == rowForChecking]:
    if beacon in noBeaconsOnRow:
        noBeaconsOnRow.remove(beacon)
        
print(f"Positions on row y={rowForChecking} with no beacons: {len(noBeaconsOnRow)}")

maxSize = [4000000, 20]["demo" in filename]
xFound = False
for y in range(maxSize + 1):
    if y % 4000 == 0:
        print("Finding distress beacon... " + str(int((y / maxSize) * 100)) + f"%", end="\r")
    ignoreRanges = []
    for sensor in sensorAreas:
        ignoreWidth = sensor[1] - abs(sensor[0][1] - y)
        if ignoreWidth > 0:
            ignoreRange = range(sensor[0][0] - ignoreWidth, sensor[0][0] + ignoreWidth + 1)
            ignoreRanges.append(ignoreRange)

    x = 0
    while x <= maxSize and not xFound:
        for ignoreRange in ignoreRanges:
            if x in ignoreRange:
                x = ignoreRange[-1] + 1
                break
        else:
            xFound = True
    if xFound:
        print("Tuning frequency of distress beacon:", (x*4000000)+y)
        break
else:
    print("Could not find the distress beacon.")