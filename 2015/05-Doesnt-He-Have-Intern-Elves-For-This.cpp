#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

const char VOWELS[] = {'a', 'e', 'i', 'o', 'u'};
const std::map<char, char> BAD = {
    {'a', 'b'},
    {'c', 'd'},
    {'p', 'q'},
    {'x', 'y'}
};

bool isNiceOne(std::string input) {
    int vowelCount = 0;
    bool hasRepeatLetter = false;
    bool hasBadString = false;
    char last = ' ';

    for (char &c : input) {
        if (std::end(VOWELS) != std::find(VOWELS, std::end(VOWELS), c)) {
            vowelCount++;
        }

        hasRepeatLetter |= c == last;
        if (BAD.find(last) != BAD.end()) {
            hasBadString |= BAD.at(last) == c;
        }

        last = c;
    }

    return vowelCount >= 3 && hasRepeatLetter && !hasBadString;
}

bool isNiceTwo(std::string input) {
    bool hasRepeatWithGap = false;
    bool hasTwoPairs = false;
    std::string firstPair;

    for (long unsigned int i = 2; i < input.length(); i++) {
        if (!hasTwoPairs) {
            firstPair = input.substr(i-2, 2);

            for (long unsigned int j = i; j < input.length(); j++) {
                if (firstPair == input.substr(j, 2)) {
                    hasTwoPairs = true;
                    break;
                }
            }
        }

        hasRepeatWithGap |= input[i - 2] == input[i];
    }

    return hasTwoPairs && hasRepeatWithGap;
}

int main() {
    int one = 0;
    int two = 0;

    while (std::cin.peek() != EOF) {
        std::string input;
        std::cin >> input;
        std::cin.get();

        one += isNiceOne(input);
        two += isNiceTwo(input);
    }

    std::cout << "Part One: " << one << std::endl;
    std::cout << "Part Two: " << two << std::endl;

    return 0;
}