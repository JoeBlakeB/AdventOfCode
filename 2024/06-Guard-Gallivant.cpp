// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 6: Guard Gallivant
// Usage:
//     scripts/cppRun.sh 2024/06-Guard-Gallivant.cpp < 2024/inputs/06.txt

#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

CharGrid simulateGuard(CharGrid map) {
    Coordinate guard = map.findFirst('^');
    Direction direction = UP;

    while (map.contains(guard)) {
        bool containsNext = map.contains(guard(direction));
        if (!containsNext || map[guard(direction)] != '#') {
            map[guard] = 'X';
            guard = guard(direction);
        } else {
            direction = turnClockwise(direction);
        }
    }
    
    return map;
}

bool simulateGuardCanLeave(CharGrid map) {
    Coordinate guard = map.findFirst('^');
    Direction direction = UP;

    while (map.contains(guard)) {
        bool containsNext = map.contains(guard(direction));
        if (!containsNext || map[guard(direction)] != '#') {
            int8_t visited = 0;
            if (map[guard] > 'a' && map[guard] <= 'a'+0xF) {
                visited = map[guard] - 'a';
                if (visited & (1 << direction)) {
                    return true;
                }
            }

            visited |= (1 << direction);

            map[guard] = 'a' + visited;
            guard = guard(direction);
        } else {
            direction = turnClockwise(direction);
        }

    }

    return false;
}

int howManyObstaclesCanCauseLoop(const CharGrid& map) {
    int count = 0;

    map.forEach([&count, map](Coordinate coordinate) {
        if (map[coordinate] == '.') {
            CharGrid newMap = map;
            newMap[coordinate] = '#';
            count += simulateGuardCanLeave(newMap);
        }
    });

    return count;
}

int main() {
    CharGrid map = {cin};
    cout << "Positions until guard leaves: " << simulateGuard(map).count('X') << endl;
    cout << "Positions the obstruction can go: " << howManyObstaclesCanCauseLoop(map) << endl;
    return 0;
}
