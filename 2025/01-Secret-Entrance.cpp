// Copyright (C) 2025 Joe Baker (JoeBlakeB)
// Advent of Code 2025 - Day 1: Secret Entrance
// Usage:
//     scripts/cppRun.sh 2025/01-Secret-Entrance.cpp < 2025/inputs/01.txt

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

vector<int> getInputRotationsVector() {
    vector<int> rotations;
    string line;
    int rotation;
    while (getline(std::cin, line) && line != "") {
        rotation = stoi(line.substr(1));
        rotations.push_back(line[0] == 'R' ? rotation : 0 - rotation);
    }
    return rotations;
}

int numberOfTimesItsZeroV1(vector<int> rotations) {
    int value = 50;
    int timesAtZero = 0;
    for (auto rotation : rotations) {
        value += rotation;
        if (value % 100 == 0) timesAtZero++;
    }
    return timesAtZero;
}

int numberOfTimesItsZeroV2(vector<int> rotations) {
    int value = 50;
    int timesAtZero = 0;
    for (auto rotation : rotations) {
        for (int i = 0; i < abs(rotation); i++) {
            value += rotation < 0 ? - 1 : 1;
            if (value < 0) value += 100;
            if (value > 99) value -= 100;
            if (value == 0) timesAtZero += 1;
        }
    }
    return timesAtZero;
}

int main() {
    auto rotations = getInputRotationsVector();
    cout << "end of instruction zeros password: " << numberOfTimesItsZeroV1(rotations) << endl;
    cout << "zeros at any click password: " << numberOfTimesItsZeroV2(rotations) << endl;
    return 0;
}
