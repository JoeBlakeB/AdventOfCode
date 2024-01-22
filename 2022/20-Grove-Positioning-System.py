#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 20: Grove Positioning System

with open("inputs/20.txt") as f:
    data = f.read().strip().split("\n")

def decrypt(data, key=1, mixCount=1):
    numbers = []
    for i in range(len(data)):
        number = str(int(data[i]) * key)
        if number in numbers:
            numbers.append(number + "#" + str(i))
        else:
            numbers.append(number)

    mixOrder = [num for num in numbers]
    for i in range(mixCount):
        for number in mixOrder:
            index = numbers.index(number)
            newIndex = (index + int(number.split("#")[0])) % (len(numbers) - 1)
            numbers.remove(number)
            numbers.insert(newIndex, number)

    sum = 0
    zeroIndex = numbers.index("0")
    for i in (1000, 2000, 3000):
        sum += int(numbers[(i + zeroIndex) % len(numbers)].split("#")[0])
    return sum

print("Part 1:", decrypt(data))
print("Part 2:", decrypt(data, 811589153, 10))
