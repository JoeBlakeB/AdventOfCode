#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

#include "utils.cpp"

class Circuit {
  public:
    void calculateWireStrengths(std::vector<std::string> unresolved) {
        while (unresolved.size() > 0) {
            unsigned int lastSize = unresolved.size();

            for (auto it = unresolved.begin(); it != unresolved.end();) {
                if (calculateInstruction(*it)) {
                    it = unresolved.erase(it);
                } else { ++it; }
            }

            if (unresolved.size() == lastSize) {
                std::cout << "\033[1;31mError: Could not resolve all signals\033[0m" << std::endl;

                std::cout << "Unresolved Wires:" << std::endl;
                for (std::string wire : unresolved)
                    std::cout << "    " << wire << std::endl;

                printValues();

                exit(1);
            }
        }
    }

    bool calculateInstruction(std::string instruction) {
        if (instruction.find("AND") != std::string::npos ||
            instruction.find("OR") != std::string::npos ||
            instruction.find("SHIFT") != std::string::npos) {
            return calculateBinary(instruction);
        } else {
            return calculateUnary(instruction);
        }
    }

    bool calculateBinary(std::string instruction) {
        std::istringstream iss(instruction);

        std::string inputName1, operation, inputName2, outputName;
        iss >> inputName1 >> operation >> inputName2 >> outputName >> outputName;

        int inputValue1 = getValue(inputName1);
        int inputValue2 = getValue(inputName2);

        if (inputValue1 == -1 || inputValue2 == -1) { return false; }

        int outputValue;

        switch (operation[0]) {
        case 'O':
            outputValue = inputValue1 | inputValue2;
            break;
        case 'A':
            outputValue = inputValue1 & inputValue2;
            break;
        case 'L':
            outputValue = inputValue1 << inputValue2;
            break;
        case 'R':
            outputValue = inputValue1 >> inputValue2;
            break;
        default:
            return false;
        }

        resolvedValues[outputName] = outputValue;
        return true;
    }

    bool calculateUnary(std::string instruction) {
        std::istringstream iss(instruction);

        std::string inputName, outputName;
        iss >> inputName;
        bool actionNot = false;
        if (inputName == "NOT") {
            iss >> inputName;
            actionNot = true;
        }
        iss >> outputName >> outputName;

        int inputValue = getValue(inputName);

        if (inputValue == -1) { return false; }

        if (actionNot) {
            inputValue = ~inputValue;
        }

        resolvedValues[outputName] = inputValue;
        return true;
    }

    int getValue(std::string nameOrValue) {
        bool isNumber = true;
        for (char character : nameOrValue) {
            isNumber &= std::isdigit(character);
        }

        if (isNumber) {
            return std::stoi(nameOrValue);
        } else if (resolvedValues.find(nameOrValue) != resolvedValues.end()) {
            return resolvedValues[nameOrValue];
        } else {
            return -1;
        }
    }

    void printValues() const {
        for (const auto &pair : resolvedValues) {
            std::cout << "Wire: " << pair.first << ", Value: " << pair.second << std::endl;
        }
    }

    std::map<std::string, unsigned short> resolvedValues;
};

int main() {
    Circuit circuit;
    std::vector<std::string> input = getInputLinesVector();

    circuit.calculateWireStrengths(input);

    int wireA = circuit.getValue("a");
    std::cout << "The signal at wireA is " << wireA << std::endl;

    circuit.resolvedValues.clear();
    circuit.resolvedValues["b"] = wireA;
    input.erase(std::remove_if(input.begin(), input.end(),
        [](const std::string &line) {
            return line.find("-> b") == line.size() - 4;
        }), input.end());
    circuit.calculateWireStrengths(input);
    
    std::cout << "Set wireB to part ones wireA signal, new wireA signal " << circuit.getValue("a") << std::endl;

    return 0;
}