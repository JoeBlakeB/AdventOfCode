#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 1: Historian Hysteria
# Usage:
#     python 2024/01-Historian-Hysteria.py < 2024/inputs/01.txt

import sys

LINES = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))

left, right = zip(*(map(int, item.split()) for item in LINES))

print("Sum of Distances:", sum(abs(a-b) for a, b in zip(sorted(list(left)), sorted(list(right)))))

print("Lists Similarity Score:", sum(item * right.count(item) for item in left))
