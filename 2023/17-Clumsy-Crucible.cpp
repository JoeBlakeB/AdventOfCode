// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2023 - Day 17: Clumsy Crucible
// Usage:
//     scripts/cppRun.sh 2023/17-Clumsy-Crucible.cpp < 2023/inputs/17.txt

#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

constexpr unsigned int MAX_UNSIGNED_INT = static_cast<unsigned int>(-1);

class DistanceGrid : public Grid<char> {
public:
    DistanceGrid(istream &input) : Grid<char>(0, 0) {
        string line;
        getline(input, line);
        _width = line.length();
        do {
            if ((int)line.length() != _width) {
                cout << "Error: Map width is not consistent" << endl;
                exit(1);
            }
            for (int i = 0; i < _width; i++) {
                map.push_back(line[i] - '0');
            }
            _height++;
        } while (getline(input, line) && line != "");
    }
};

int shortestPathDistance(DistanceGrid &map, Coordinate start, Coordinate end, short MINIMUM_SPEED = -1, short MAXIMUM_SPEED = 3) {
    vector<unsigned int> distancesDefalts(4*(MAXIMUM_SPEED+1), MAX_UNSIGNED_INT);
    Grid<vector<unsigned int>> distances(map.width, map.height, distancesDefalts);

    typedef tuple<unsigned int, Coordinate, char, char> QueueItem;
    priority_queue<QueueItem, vector<QueueItem>, greater<QueueItem>> queue;
    
    for (short i = 0; i < 4; i++) {
        queue.push({0, start, i, 0});
    }

    while (!queue.empty()) {
        auto [currentDistance, current, direction, speed] = queue.top();
        queue.pop();

        Coordinate neighbors[4] = {
            {current.x, current.y-1},
            {current.x-1, current.y},
            {current.x, current.y+1},
            {current.x+1, current.y}
        };

        for (short i = 0; i < 4; i++) {
            if (speed < MINIMUM_SPEED && i != direction) {
                continue; // Cannot turn without going at least the minimum speed
            }

            if ((i - direction + 2) % 4 == 0) {
                continue; // Cannot turn 180 degrees
            }

            short newSpeed = (speed * (direction == i)) + 1;
            
            if (newSpeed > MAXIMUM_SPEED) {
                continue; // Cannot go faster than the maximum speed without turning
            }

            Coordinate neighbor = neighbors[i];

            if (neighbor.x < 0 || neighbor.y < 0 || 
                neighbor.x >= map.width || neighbor.y >= map.height) {
                continue; // Cannot go out of bounds
            }

            unsigned int distance = currentDistance + map(neighbor);

            if (distance >= distances(neighbor)[direction + (newSpeed * 4)]) {
                continue; // Cannot enter a cell when going slower than last time, we can already go faster to this point
            }

            if (neighbor == end && newSpeed >= MINIMUM_SPEED) {
                return distance;
            } else {
                distances(neighbor)[direction + (newSpeed * 4)] = distance;
                queue.push({distance, neighbor, i, newSpeed});
            }
        }
    }

    return 0;
}

int main() {
    DistanceGrid map = DistanceGrid(cin);
    cout << "Shortest path distance: " << shortestPathDistance(map, {0, 0}, {map.width-1, map.height-1}) << endl;
    cout << "With an Ultra Cricible: " << shortestPathDistance(map, {0, 0}, {map.width-1, map.height-1}, 4, 10) << endl;
    return 0;
}
