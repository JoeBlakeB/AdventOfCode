#!/usr/bin/env python3

# Day 13: Distress Signal

import sys

if "-v" in sys.argv:
    log = print
else:
    log = lambda *a, **k: None

with open("inputs/13.txt") as f:
    data = f.read().strip()

class Packet:
    def __init__(self, data):
        self.data = eval(data)

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.compare(self.data, other.data)

    def compare(self, a, b, depth=0):
        log(" "*(depth), "Compare", a, "vs", b)
        if type(a) == int and type(b) == int:
            if a < b:
                log(" "*(depth+2), "Right order - left input is smaller")
                return True
            elif a > b:
                log(" "*(depth+2), "Wrong order - right input is smaller")
                return False
        elif type(a) == list and type(b) == list:
            for i in range(len(a)):
                if i >= len(b):
                    log(" "*(depth+2),"Wrong order - right LIST is shorter")
                    return False
                compared = self.compare(a[i], b[i], depth=depth+1)
                if type(compared) == bool:
                    return compared
            if len(a) < len(b):
                log(" "*(depth+2), "Right order - left LIST is shorter")
                return True
        else:
            if type(a) == int:
                a = [a]
            if type(b) == int:
                b = [b]
            return self.compare(a, b, depth=depth+1)

# Part 1
packetPairs = [line.split("\n") for line in data.split("\n\n")]
sumOfIndices = 0
for i in range(len(packetPairs)):
    a, b = [Packet(packet) for packet in packetPairs[i]]
    log("== Pair", i+1, "==")
    if a < b:
        sumOfIndices += i + 1
print("The sum of indiciess in the correct order is:", sumOfIndices)

# Part 2
dividers = ["[[2]]", "[[6]]"]
packets = [Packet(divider) for divider in dividers]
for packet in data.split("\n"):
    if packet:
        packets.append(Packet(packet))
packets.sort()
packetsOrdered = [str(packet) for packet in packets]
log("\n".join(packetsOrdered))
decoderKey = 1
for i in range(len(packetsOrdered)):
    if packetsOrdered[i] in dividers:
        decoderKey *= i + 1
print("The decoder key is:", decoderKey)