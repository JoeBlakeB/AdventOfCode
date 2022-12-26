#!/usr/bin/env python3

# Day 25: Full of Hot Air

with open("inputs/25.txt") as f:
    data = f.read().strip().split("\n")

digits = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

def snafuToDecimal(snafu):
    total = 0
    power = 1
    for digit in snafu[::-1]:
        total += digits[digit] * power
        power *= 5
    return total

def decimalToSnafu(decimal):
    snafu = ""
    i = 0
    while decimal >= 5**i:
        num = decimal // (5**i) % 5
        snafu += "012=-"[num]
        if num > 2:
            decimal += ((0-num) + (5**(i+1)))
        else:
            decimal -= num * (5**i)
        i += 1
    return snafu[::-1]

print("SNAFU number to enter into Bob's console:",
    decimalToSnafu(sum([snafuToDecimal(num) for num in data])))
