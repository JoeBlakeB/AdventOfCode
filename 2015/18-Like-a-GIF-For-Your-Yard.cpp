#include <iostream>
#include <vector>

#include "utils.cpp"

using namespace std;

constexpr int GRID_SIZE = 100;

class LightGrid {
public:
    LightGrid() {
        currentLights = new int[GRID_SIZE * GRID_SIZE];
        tempLights = new int[GRID_SIZE * GRID_SIZE];
    }
    LightGrid(const vector<string>& input) : LightGrid() {
        for (int x = 0; x < GRID_SIZE; x++) {
        for (int y = 0; y < GRID_SIZE; y++) {
            currentLights[x * GRID_SIZE + y] = input[x][y] == '#' ? 1 : 0;
        }}
    }
    ~LightGrid() {
        delete[] currentLights;
        delete[] tempLights;
    }
    LightGrid(const LightGrid& other) = delete;
    LightGrid& operator=(const LightGrid& other) = delete;

    string to_string() const {
        string result;
        for (int x = 0; x < GRID_SIZE; x++) {
            for (int y = 0; y < GRID_SIZE; y++) {
                result += currentLights[x * GRID_SIZE + y] ? '#' : '.';
            }
            result += '\n';
        }
        return result;
    }

    void doStep() {
        for (int x = 0; x < GRID_SIZE; x++) {
        for (int y = 0; y < GRID_SIZE; y++) {
            int surroundingCount = 0;
            for (int x2 = -1; x2 <= 1; x2++) {
            for (int y2 = -1; y2 <= 1; y2++) {
                if ((x2 == 0 && y2 == 0)
                  || x + x2 < 0 || x + x2 >= GRID_SIZE
                  || y + y2 < 0 || y + y2 >= GRID_SIZE) continue;

                if (currentLights[(x + x2) * GRID_SIZE + (y + y2)]) surroundingCount++;
            }}

            if (currentLights[x * GRID_SIZE + y]) {
                tempLights[x * GRID_SIZE + y] = surroundingCount == 2 || surroundingCount == 3;
            } else {
                tempLights[x * GRID_SIZE + y] = surroundingCount == 3;
            }
        }}

        swap(currentLights, tempLights);
    }

    unsigned int countLit() {
        int litCount = 0;
        for (int x = 0; x < GRID_SIZE; x++) {
        for (int y = 0; y < GRID_SIZE; y++) {
            if (currentLights[x * GRID_SIZE + y]) litCount++;
        }}
        return litCount;
    }

    void turnCornersOn() {
        currentLights[0] = true;
        currentLights[GRID_SIZE - 1] = true;
        currentLights[GRID_SIZE * GRID_SIZE - GRID_SIZE] = true;
        currentLights[GRID_SIZE * GRID_SIZE - 1] = true;
    }

private:
    int* currentLights, * tempLights;
};

int main() {
    vector<string> inputVector = getInputLinesVector();
    {
        LightGrid lightGrid(inputVector);
        
        for (int i = 0; i < 100; i++) {
            lightGrid.doStep();
        }

        cout << "Part one lights lit: " << lightGrid.countLit() << endl;
    }
    {
        LightGrid lightGrid = LightGrid(inputVector);
        
        for (int i = 0; i < 100; i++) {
            lightGrid.turnCornersOn();
            lightGrid.doStep();
        }
        lightGrid.turnCornersOn();

        cout << "Part two lights lit: " << lightGrid.countLit() << endl;
    }
    return 0;
}