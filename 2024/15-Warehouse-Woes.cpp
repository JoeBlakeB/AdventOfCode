// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 15: Warehouse Woes
// Usage:
//     scripts/cppRun.sh 2024/15-Warehouse-Woes.cpp < 2024/inputs/15.txt

#include <iostream>
#include <queue>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

vector<Direction> getMovements() {
    vector<Direction> directions;
    string line;
    while (getline(std::cin, line) && line != "") {
        for(char movement : line) {
            switch (movement) {
              case '^':
                directions.push_back(UP);
                break;
            case 'v':
                directions.push_back(DOWN);
                break;
            case '<':
                directions.push_back(LEFT);
                break;
            case '>':
                directions.push_back(RIGHT);
                break;
            }
        }
    }
    return directions;
}

void doMovement(CharGrid& warehouseMap, Coordinate& robot, Direction direction) {
    int positionsToMove = 0;
    bool canMove = false;
    Coordinate nextMove = robot(direction);
    char nextMoveChar = warehouseMap[nextMove];

    while (nextMoveChar != '#') {
        positionsToMove++;
        if (nextMoveChar == '.') {
            canMove = true;
            break;
        }
        nextMove = nextMove(direction);
        nextMoveChar = warehouseMap[nextMove];
    }

    if (canMove) {
        for (int i = positionsToMove; i > 1; i--) {
            warehouseMap[nextMove] = warehouseMap[nextMove(turn180Degrees(direction))];
            nextMove = nextMove(turn180Degrees(direction));
        }

        warehouseMap[robot] = '.';
        robot = robot(direction);
        warehouseMap[robot] = '@';
    }
}

void addToVectorIfNotAlreadyIn(vector<Coordinate>& vec, Coordinate& coord) {
    if (find(vec.begin(), vec.end(), coord) == vec.end()) {
        vec.push_back(coord);
    }
}

void doMovementWideBoxes(CharGrid& warehouseMap, Coordinate& robot, Direction direction) {
    CharGrid mapNext = warehouseMap;
    vector<Coordinate> boxesInPreviousRow = {robot};
    vector<Coordinate> boxesInNextRow;

    while (boxesInPreviousRow.size()) {
        for (Coordinate coord : boxesInPreviousRow) {
            Coordinate nextCoord = coord(direction);
            mapNext[nextCoord] = warehouseMap[coord]+1;

            switch (warehouseMap[nextCoord]) {
              case '.':
                break;
              case '#':
                return;
              case '[':
                addToVectorIfNotAlreadyIn(boxesInNextRow, nextCoord);
                nextCoord = nextCoord(RIGHT);
                if (mapNext[nextCoord] != '['+1 && mapNext[nextCoord] != ']'+1) {
                    mapNext[nextCoord] = '.';
                }
                addToVectorIfNotAlreadyIn(boxesInNextRow, nextCoord);
                break;
              case ']':
                addToVectorIfNotAlreadyIn(boxesInNextRow, nextCoord);
                nextCoord = nextCoord(LEFT);
                if (mapNext[nextCoord] != '['+1 && mapNext[nextCoord] != ']'+1) {
                    mapNext[nextCoord] = '.';
                }
                addToVectorIfNotAlreadyIn(boxesInNextRow, nextCoord);
                break;
            }
        }
        boxesInPreviousRow = boxesInNextRow;
        boxesInNextRow.clear();
    }

    warehouseMap.replace(mapNext);
    warehouseMap.forEach([&warehouseMap](Coordinate coord) {
        if (warehouseMap[coord] == '['+1 || warehouseMap[coord] == ']'+1) {
            warehouseMap[coord]--;
        }
    });
    warehouseMap[robot] = '.';
    robot = robot(direction);
    warehouseMap[robot] = '@';
}

int getBoxGPSSum(const CharGrid& warehouseMap) {
    return warehouseMap.sumEach<int>([&warehouseMap](Coordinate coord) {
        if (warehouseMap[coord] == 'O' || warehouseMap[coord] == '[') {
            return (100 * coord.y) + coord.x;
        }
        return 0;
    });
}

CharGrid createSecondWarehouse(const CharGrid& warehouseMap) {
    CharGrid secondMap(warehouseMap.width*2, warehouseMap.height, '.');

    warehouseMap.forEach([&warehouseMap, &secondMap](Coordinate coord) {
        switch (warehouseMap[coord]) {
          case '#':
            secondMap(coord.x*2, coord.y) = '#';
            secondMap((coord.x*2)+1, coord.y) = '#';
            break;
          case 'O':
            secondMap(coord.x*2, coord.y) = '[';
            secondMap((coord.x*2)+1, coord.y) = ']';
            break;
          case '@':
            secondMap(coord.x*2, coord.y) = '@';
            break;
        }
    });

    return secondMap;
}

int main() {
    CharGrid warehouseMap = {cin};
    CharGrid secondMap = createSecondWarehouse(warehouseMap);

    vector<Direction> movements = getMovements();

    Coordinate robot1 = warehouseMap.findFirst('@');
    Coordinate robot2 = secondMap.findFirst('@');
    for(Direction direction : movements) {
        doMovement(warehouseMap, robot1, direction);

        if (direction % 2 == 0) {
            doMovementWideBoxes(secondMap, robot2, direction);
        } else {
            doMovement(secondMap, robot2, direction);
        }
    }

    cout << "GPS sum in first warehouse: " << getBoxGPSSum(warehouseMap) << endl;
    cout << "GPS sum in second warehouse: " << getBoxGPSSum(secondMap) << endl;

    return 0;
}
