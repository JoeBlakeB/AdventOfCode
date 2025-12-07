// Copyright (C) 2025 Joe Baker (JoeBlakeB)
// Advent of Code 2025 - Day 7: Laboratories
// Usage:
//     scripts/cppRun.sh 2025/07-Laboratories.cpp < 2025/inputs/07.txt

#include <iostream>
#include <string>
#include <vector>
#include <cstdint>

#include "../Utils/Grid.cpp"

using namespace std;

int main() {
    CharGrid tachyonManifolds = {cin};
    Grid<int64_t> timelines(tachyonManifolds.width, tachyonManifolds.height);
    timelines(tachyonManifolds.findFirst('S')) = 1;
    int splitterHits = 0;
    int64_t totalTimelines = 1;

    timelines.forEach([&](Coordinate c) {
        if (timelines[c] != 0) {
            if (tachyonManifolds[c(DOWN)] == '^') {
                splitterHits++;
                totalTimelines += timelines[c];
                timelines[c(DOWN)(LEFT)] += timelines[c];
                timelines[c(DOWN)(RIGHT)] += timelines[c];
            } else {
                timelines[c(DOWN)] += timelines[c];
            }
        }
    });

    cout << "splitters: " << splitterHits << endl;
    cout << "timelines: " << totalTimelines << endl;

    return 0;
}
