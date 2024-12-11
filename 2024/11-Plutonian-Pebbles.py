#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 11: Plutonian Pebbles
# Usage:
#     python 2024/11-Plutonian-Pebbles.py < 2024/inputs/11.txt

from collections import defaultdict

PEBBLE_INPUT = [int(p) for p in input().split(" ")]
pebbles = {p: PEBBLE_INPUT.count(p) for p in set(PEBBLE_INPUT)}

def blink(pebbles: dict[int: int]):
    newPebbles = defaultdict(int)
    for pebble, count in pebbles.items():
        if pebble == 0:
            newPebbles[1] += count
        elif len(str(pebble)) % 2 == 0:
            pebbleStr = str(pebble)
            newPebbles[int(pebbleStr[:len(pebbleStr)//2])] += count
            newPebbles[int(pebbleStr[len(pebbleStr)//2:])] += count
        else:
            newPebbles[2024*pebble] += count
    return newPebbles

for i in range(25):
    pebbles = blink(pebbles)

print("Pebbles after 25 blinks:", sum(pebbles.values()))

for i in range(50):
    pebbles = blink(pebbles)
    
print("Pebbles after 75 blinks:", sum(pebbles.values()))
