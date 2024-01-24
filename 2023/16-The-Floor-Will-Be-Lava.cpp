// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2023 - Day 16: The Floor Will Be Lava
// Usage:
//     scripts/cppRun.sh 2023/16-The-Floor-Will-Be-Lava.cpp < 2023/inputs/16.txt

#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

unsigned int countEnergizedTiles(const CharGrid& contraption, Coordinate startCoord = {-1, 0}, Direction startDirection = RIGHT) {
    struct EnergizedTile { bool horizontal; bool vertical; };
    Grid<EnergizedTile> energized(contraption.width, contraption.height, {false, false});

    stack<pair<Coordinate, Direction>> stack;
    stack.push({startCoord, startDirection});

    while (!stack.empty()) {
        auto [coord, direction] = stack.top();
        stack.pop();

        Coordinate nextCoord = coord(direction);
        char character = contraption[nextCoord];

        if (!contraption.contains(nextCoord)) {
            continue;
        }

        bool horizontal = direction == LEFT || direction == RIGHT;

        bool& energizedTile = horizontal ? energized[nextCoord].horizontal : energized[nextCoord].vertical;
        if (energizedTile && character == '.') {
            continue;
        }
        energizedTile = true;

        if (character == '|' && horizontal) {
            stack.push({nextCoord, UP});
            stack.push({nextCoord, DOWN});
        } else if (character == '-' && !horizontal) {
            stack.push({nextCoord, LEFT});
            stack.push({nextCoord, RIGHT});
        } else if ((character == '/' && direction == UP) || (character == '\\' && direction == DOWN)) {
            stack.push({nextCoord, RIGHT});
        } else if ((character == '/' && direction == DOWN) || (character == '\\' && direction == UP)) {
            stack.push({nextCoord, LEFT});
        } else if ((character == '/' && direction == LEFT) || (character == '\\' && direction == RIGHT)) {
            stack.push({nextCoord, DOWN});
        } else if ((character == '/' && direction == RIGHT) || (character == '\\' && direction == LEFT)) {
            stack.push({nextCoord, UP});
        } else {
            stack.push({nextCoord, direction});
        }
    }

    return count_if(energized.begin(), energized.end(), [](EnergizedTile tile) {
        return tile.horizontal || tile.vertical;
    });
}

unsigned int findHighestPossibleRow(
    const CharGrid& contraption,
    int startX, int endX,
    int startY, int endY,
    Direction direction
) {
    unsigned int maxEnergized = 0;
    for (int y = startY; y <= endY; y++) {
        for (int x = startX; x <= endX; x++) {
            maxEnergized = max(maxEnergized, countEnergizedTiles(contraption, {x, y}, direction));
        }
    }
    return maxEnergized;
}

unsigned int findHighestPossible(const CharGrid& contraption) {
    return max(
        max(
            findHighestPossibleRow(contraption, -1, -1, 0, contraption.height, RIGHT),
            findHighestPossibleRow(contraption, contraption.width, contraption.width, 0, contraption.height, LEFT)
        ),
        max(
            findHighestPossibleRow(contraption, 0, contraption.width, -1, -1, DOWN),
            findHighestPossibleRow(contraption, 0, contraption.width, contraption.height, contraption.height, UP)
        )
    );
}

int main() {
    CharGrid contraption(cin);
    cout << "Energized Tile Count: " << countEnergizedTiles(contraption) << endl;
    cout << "Highest Energy Possible: " << findHighestPossible(contraption) << endl;
    return 0;
}
