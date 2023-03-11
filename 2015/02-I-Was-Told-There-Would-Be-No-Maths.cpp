#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

int calculateWrappingPaper(int dimensions[3]) {
    int areas[3] = {
        dimensions[0] * dimensions[1],
        dimensions[1] * dimensions[2],
        dimensions[2] * dimensions[0]
    };

    int minArea = areas[0];
    int totalArea = minArea * 2;
    for (int i = 1; i < 3; i++) {
        if (areas[i] < minArea) {
            minArea = areas[i];
        }
        totalArea += areas[i] * 2;
    }

    return totalArea + minArea;
}

int calculateRibbon(int dimensions[3]) {
    std::sort(dimensions, dimensions + 3);
    return (dimensions[0] * 2) + (dimensions[1] * 2) +
           (dimensions[0] * dimensions[1] * dimensions[2]);
}

int main() {
    int totalWrappingPaper = 0;
    int totalRibbon = 0;

    while (std::cin.peek() != EOF) {
        std::string input;
        std::cin >> input;
        std::cin.get();
        std::stringstream ss(input);
        std::string token;

        int dimensions[3];
        for (int i = 0; i < 3; i++) {
            std::getline(ss, token, 'x');
            dimensions[i] = std::stoi(token);
        }

        totalWrappingPaper += calculateWrappingPaper(dimensions);
        totalRibbon += calculateRibbon(dimensions);
    }

    std::cout << "You need " << totalWrappingPaper <<
        " square feet of wrapping paper\nand " <<
        totalRibbon << " feet of ribbon" << std::endl;

    return 0;
}