#include <iostream>
#include <sstream>

const int GRID_WIDTH = 1000;
const int GRID_HEIGHT = 1000;

class Grid1 {
  public:
    void setLights(int xFrom, int yFrom, int xTo, int yTo, bool state) {
        for (int y = yFrom; y <= yTo; y++) {
            for (int x = xFrom; x <= xTo; x++) {
                grid[(y * GRID_WIDTH) + x] = state;
            }
        }
    }

    void toggleLights(int xFrom, int yFrom, int xTo, int yTo) {
        for (int y = yFrom; y <= yTo; y++) {
            for (int x = xFrom; x <= xTo; x++) {
                grid[(y * GRID_WIDTH) + x] ^= true;
            }
        }
    }

    int litCount() {
        int count = 0;
        for (int i = 0; i < GRID_WIDTH * GRID_HEIGHT; i++) {
            if (grid[i]) { count++; }
        }
        return count;
    }
    
  private:
    bool grid[GRID_WIDTH * GRID_HEIGHT] = {false};
};

class Grid2 {
  public:
    void changeBrightness(int xFrom, int yFrom, int xTo, int yTo, int increase) {
        for (int y = yFrom; y <= yTo; y++) {
            for (int x = xFrom; x <= xTo; x++) {
                int gridLocation = (y * GRID_WIDTH) + x;
                int brightness = grid[gridLocation] + increase;
                if (brightness < 0) { brightness = 0; }
                grid[gridLocation] = brightness;
            }
        }
    }

    int totalBrightness() {
        int count = 0;
        for (int i = 0; i < GRID_WIDTH * GRID_HEIGHT; i++) {
            count += grid[i];
        }
        return count;
    }

  private:
    int grid[GRID_WIDTH * GRID_HEIGHT] = {false};
};

int main() {
    Grid1 grid1;
    Grid2 grid2;
    std::string instruction;

    while (std::getline(std::cin, instruction)) {
        std::stringstream ss(instruction);

        std::string action;
        bool turnOn = false;
        ss >> action;
        if (action == "turn") {
            std::string onOrOff;
            ss >> onOrOff;
            turnOn = onOrOff == "on";
        }

        int xFrom, yFrom, xTo, yTo;
        char commaIgnore;
        std::string throughIgnore;
        ss >> xFrom >> commaIgnore >> yFrom >> 
            throughIgnore >> xTo >> commaIgnore >> yTo;

        if (action == "turn") {
            grid1.setLights(xFrom, yFrom, xTo, yTo, turnOn);
            grid2.changeBrightness(xFrom, yFrom, xTo, yTo, turnOn ? 1 : -1);
        } else {
            grid1.toggleLights(xFrom, yFrom, xTo, yTo);
            grid2.changeBrightness(xFrom, yFrom, xTo, yTo, 2);
        }
    }

    std::cout << "There are " << grid1.litCount() << " lights lit in part one" << std::endl;
    std::cout << "The total brightness is " << grid2.totalBrightness() << " for part two" << std::endl;
    return 0;
}