// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2023 - Day 15: Lens Library
// Usage:
//     scripts/cppRun.sh 2023/15-Lens-Library.cpp < 2023/inputs/15.txt

#include <array>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

unsigned char holidayASCIIStringHelperAlgorithm(const string& sequence) {
    unsigned char value = 0;

    for (const char& character : sequence) {
        value += character;
        value *= 17;
    }

    return value;
}

void forEachStep(const string& sequence, const function<void(const string&)>& callback) {
    int stepStart = 0;

    for (size_t i = 1; i <= sequence.length(); i++) {
        if (sequence[i] == ',' || i == sequence.length()) {
            callback(sequence.substr(stepStart, i - stepStart));
            stepStart = i + 1;
        }
    }
}

int sumHashes(const string& sequence) {
    int sum = 0;

    forEachStep(sequence, [&sum](const string& step) {
        sum += holidayASCIIStringHelperAlgorithm(step);
    });

    return sum;
}

int calculateFocusingPower(const string& sequence) {
    typedef vector<pair<string, unsigned char>> Box;
    array<Box, 256> boxes;

    forEachStep(sequence, [&boxes](const string& step) {
        bool removeOperation = false;
        if (step[step.length() - 1] == '-') { removeOperation = true; }

        string label = step.substr(0, step.length() - 2 + removeOperation);
        Box& box = boxes[holidayASCIIStringHelperAlgorithm(label)];

        int lensIndex = -1;
        for (size_t i = 0; i < box.size(); i++) {
            if (box[i].first == label) {
                lensIndex = i;
                break;
            }
        }

        if (removeOperation) {
            if (lensIndex != -1) {
                box.erase(box.begin() + lensIndex);
            }
        } else {
            unsigned char focalLength = step[step.length() - 1] - '0';
            if (lensIndex != -1) {
                box[lensIndex].second = focalLength;
            } else {
                box.push_back({label, focalLength});
            }
        }

    });

    int focusingPower = 0;
    for (size_t b = 0; b < boxes.size(); b++) {
        for (size_t s = 0; s < boxes[b].size(); s++) {
            focusingPower += (b + 1) * (s + 1) * boxes[b][s].second;
        }
    }

    return focusingPower;
}

int main() {
    string sequence;
    getline(cin, sequence);
    cout << "Sum of HASHes: " << sumHashes(sequence) << endl;
    cout << "Focusing Power: " << calculateFocusingPower(sequence) << endl;
    return 0;
}
