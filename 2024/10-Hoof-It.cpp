// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 10: Hoof It
// Usage:
//     scripts/cppRun.sh 2024/10-Hoof-It.cpp < 2024/inputs/10.txt

#include <iostream>
#include <queue>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

int getTrailCountFrom(const CharGrid& map, Coordinate start, bool skipEndsCheck) {
    queue<Coordinate> trail({start});
    vector<Coordinate> ends;
    int trailCount = 0;

    while (!trail.empty()) {
        auto current = trail.front();
        trail.pop();

        for (Direction direction : {UP, RIGHT, DOWN, LEFT}) {
            Coordinate next = current(direction);
            if (!map.contains(next)) continue;
            
            if ((map[next] == map[current] + 1)) {
                if (map[next] == '9') {
                    if (skipEndsCheck || find(ends.begin(), ends.end(), next) == ends.end()) {
                        ends.push_back(next);
                        trailCount++;
                    }
                } else {
                    trail.push(next);
                }
            }
        }
    }

    return trailCount;
}

int getTrailCountSum(const CharGrid& map, bool skipEndsCheck) {
    int totalTrailCount = 0;
    map.forEach([&map, &totalTrailCount, &skipEndsCheck](Coordinate coord) {
        if (map[coord] == '0') {
            totalTrailCount += getTrailCountFrom(map, coord, skipEndsCheck);
        }
    });
    return totalTrailCount;
}

int main() {
    const CharGrid map = {cin};

    cout << "Trailhead unique ends rating sum: " << getTrailCountSum(map, false) << endl;
    cout << "Trailhead total rating sum: " << getTrailCountSum(map, true) << endl;

    return 0;
}
