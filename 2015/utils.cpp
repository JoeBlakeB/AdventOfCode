#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> getInputLinesVector() {
    vector<string> inputLines;
    string line;
    while (getline(std::cin, line) && line != "") {
        inputLines.push_back(line);
    }
    return inputLines;
}