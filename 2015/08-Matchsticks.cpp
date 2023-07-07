#include <iostream>
#include <vector>

#include "utils.cpp"

std::string decodeString(std::string original) {
    std::string decodedString = "";
    for (unsigned int i = 1; i < original.size() - 1; ++i) {
        if (original[i] == '\\') {
            if (original[i+1] == 'x') {
                decodedString += static_cast<char>(
                    std::stoi(original.substr(i+2, 2), nullptr, 16));
                i += 3;
            } else {
                decodedString += original[++i];
            }
        } else {
            decodedString += original[i];
        }
    }
    return decodedString;
}

std::string encodeString(std::string original) {
    std::string encodedString = "\"";
    for (unsigned int i = 0; i < original.size(); ++i) {
        if (original[i] == '"' || original[i] == '\\') {
            encodedString += '\\';
        }
        encodedString += original[i];
    }
    return encodedString + '\"';
}

int main() {
    std::vector<std::string> inputLines = getInputLinesVector();
    unsigned int originalSize = 0;
    unsigned int decodedSize = 0;
    unsigned int encodedSize = 0;

    for (std::string line : inputLines) {
        originalSize += line.size();
        decodedSize += decodeString(line).size();
        encodedSize += encodeString(line).size();
    }

    std::cout << "Original Length: " << originalSize << std::endl;
    std::cout << "Decoded Length: " << decodedSize << " (difference: "
              << (originalSize - decodedSize) << ")" << std::endl;
    std::cout << "Encoded Length: " << encodedSize << " (difference: "
              << (encodedSize - originalSize) << ")" << std::endl;

    return 0;
}