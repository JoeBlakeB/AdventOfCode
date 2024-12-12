// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 12: Garden Groups
// Usage:
//     scripts/cppRun.sh 2024/12-Garden-Groups.cpp < 2024/inputs/12.txt

#include <iostream>
#include <queue>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

template <bool sidesDiscount>
int calculateFenceCost(CharGrid garden) {
    return garden.sumEach<int>([&garden](Coordinate coord) {
        if (!garden[coord]) {
            return 0;
        }

        int area = 1;
        int perimeter = 0;
        char plant = garden[coord];
        queue<Coordinate> regionQueue({coord});
        CharGrid region(garden.width, garden.height, 0);
        region[coord] = 1;
        garden[coord] = 0;
        
        while (!regionQueue.empty()) {
            auto current = regionQueue.front();
            regionQueue.pop();

            for (Direction direction : {UP, RIGHT, DOWN, LEFT}) {
                Coordinate next = current(direction);
                if (garden.contains(next)) {
                    if (garden[next] == plant) {
                        region[next] = 1;
                        garden[next] = 0;
                        area++;
                        regionQueue.push(next);
                    } else if (!region[next]) {
                        if constexpr(!sidesDiscount) {
                            perimeter++;
                        }
                    }
                } else {
                    if constexpr(!sidesDiscount) {
                        perimeter++;
                    }
                }
            }
        }

        if constexpr(sidesDiscount) {
            auto checkSide = [&perimeter, &region](int x, int y, int x2, int y2, bool& sideDetected) {
                if (region(x, y) && !(region.contains(x2, y2) ? region(x2, y2) : 0)) {
                    if (!sideDetected) {
                        perimeter++;
                        sideDetected = true;
                    }
                } else {
                    sideDetected = false;
                }
            };

            for (int y = 0; y < region.height; y++) {
                bool topSide = false, bottomSide = false;
                for (int x = 0; x < region.width; x++) {
                    checkSide(x, y, x, y-1, topSide);
                    checkSide(x, y, x, y+1, bottomSide);
                }
            }
            
            for (int x = 0; x < region.width; x++) {
                bool leftSide = false, rightSide = false;
                for (int y = 0; y < region.height; y++) {
                    checkSide(x, y, x-1, y, leftSide);
                    checkSide(x, y, x+1, y, rightSide);
                }
            }
        }

        return area * perimeter;
    });
}

int main() {
    const CharGrid garden = {cin};

    cout << "Fence cost with perimeter: " << calculateFenceCost<false>(garden) << endl;
    cout << " with sides bulk discount: " << calculateFenceCost<true>(garden) << endl;

    return 0;
}
