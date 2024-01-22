#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 6: Tuning Trouble

with open("inputs/06.txt") as f:
    data = f.read().strip()


def lookForMarker(data, markerLength):
    markerAfter = 0
    for i in range(len(data) - markerLength - 1):
        fourRecent = data[i:i+markerLength]
        for char in fourRecent:
            if fourRecent.count(char) != 1:
                break
        else:
            markerAfter = i + markerLength
            break
    return markerAfter

print("Packet: ", lookForMarker(data, 4))
print("Message:", lookForMarker(data, 14))