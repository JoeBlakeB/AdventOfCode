#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 17: Chronospatial Computer
# Usage:
#     python 2024/17-Chronospatial-Computer.py < 2024/inputs/17.txt

class Computer:
    instructionPointer = 0
    stdout: list[int] = []

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def __repr__(self):
        return f"Computer({self.a}, {self.b}, {self.c})"

    def executeProgram(self, program: list[int]):
        self.instructionPointer = 0
        self.stdout.clear()
        while self.instructionPointer + 1 < len(program):
            instruction = self.getInstruction(program[self.instructionPointer])
            operand = program[self.instructionPointer+1]
            instruction(operand)
            self.instructionPointer += 2
        return ",".join((str(i) for i in self.stdout))

    def xdv(self, operand: int):
        numerator = self.a
        denominator = 2 ** self.combo(operand)
        return numerator // denominator

    def adv(self, operand: int):
        self.a = self.xdv(operand)

    def bxl(self, operand: int):
        self.b = self.b ^ operand

    def bst(self, operand: int):
        self.b = self.combo(operand) % 8

    def jnz(self, operand: int):
        if self.a != 0:
            self.instructionPointer = operand - 2

    def bxc(self, operand: int):
        self.b = self.b ^ self.c

    def out(self, operand: int):
        self.stdout.append(self.combo(operand) % 8)

    def bdv(self, operand: int):
        self.b = self.xdv(operand)

    def cdv(self, operand: int):
        self.c = self.xdv(operand)
    
    def getInstruction(self, opcode):
        return [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        ][opcode]
    
    def combo(self, operand):
        if operand < 4: return operand
        return [self.a, self.b, self.c][operand-4]

computer = Computer(*(int(r.split(": ")[1]) for r in (input(), input(), input(), input())[:3]))
program = [int(i) for i in input().split(": ")[1].split(",")]
print("Program Output:", computer.executeProgram(program))
