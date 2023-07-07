#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> getInputLinesVector() {
    std::vector<std::string> inputLines;
    std::string line;
    while (std::getline(std::cin, line)) {
        inputLines.push_back(line);
    }
    return inputLines;
}