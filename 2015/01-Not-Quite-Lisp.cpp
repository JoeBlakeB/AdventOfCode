// Copyright (C) 2023 Joe Baker (JoeBlakeB)
// Advent of Code 2015 - Day 01: Not Quite Lisp
// Usage:
//     scripts/cppRun.sh 2015/01-Not-Quite-Lisp.cpp < 2015/inputs/01.txt

#include <iostream>

int main() {
    std::string input;
    std::cin >> input;

    int floorNum = 0;
    int firstReachBasement = 0;
    for (long unsigned int i = 0; i < input.length(); i++) {
        if (input[i] == '(') {
            floorNum++;
        } else if (input[i] == ')') {
            floorNum--;
        }

        if (floorNum < 0 && !firstReachBasement) {
            firstReachBasement = i + 1;
        }
    }

    std::cout << "You are on floor # " << floorNum << std::endl;
    std::cout << "You first reach the basement at position # " << firstReachBasement << std::endl;
    return 0;
}