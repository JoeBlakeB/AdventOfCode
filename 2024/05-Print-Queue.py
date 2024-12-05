#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 5: Print Queue
# Usage:
#     python 2024/05-Print-Queue.py < 2024/inputs/05.txt

import sys
from collections import defaultdict

pageOrderingRulesStrings = [rule.split("|") for rule in iter(lambda: next(sys.stdin).rstrip("\n"), "")]
PAGE_ORDERING_RULES = defaultdict(list)
for before, after in pageOrderingRulesStrings:
    PAGE_ORDERING_RULES[before].append(after)

class Page:
    def __init__(self, pageNumber: str):
        self.pageNumber = str(pageNumber)

    def __repr__(self) -> str:
        return f"Page({self.pageNumber})"
    
    def __str__(self) -> str:
        return self.pageNumber
    
    def __int__(self) -> int:
        return int(self.pageNumber)
    
    def __eq__(self, value: object) -> bool:
        return str(self) == str(value)
    
    def __lt__(a: "Page", b: "Page"):
        if a in PAGE_ORDERING_RULES and b in PAGE_ORDERING_RULES[a]:
            return True
        if b in PAGE_ORDERING_RULES and a in PAGE_ORDERING_RULES[b]:
            return False
        return a.pageNumber < b.pageNumber
    
    def __hash__(self):
        return hash(self.pageNumber)

updatesToProduce = [[Page(page) for page in line.split(",")] for line in iter(lambda: next(sys.stdin).rstrip("\n"), "")]
updatesSorted = [sorted(update) for update in updatesToProduce]

correctlyOrderedSum = 0
incorrectlyOrderedSum = 0

for orig, correct in zip(updatesToProduce, updatesSorted):
    if orig == correct:
        correctlyOrderedSum += int(orig[len(orig) // 2])
    else:
        incorrectlyOrderedSum += int(correct[len(correct) // 2])

print("The sum of middle pages when")
print("    correctly ordered:", correctlyOrderedSum)
print("    incorrectly ordered:", incorrectlyOrderedSum)
