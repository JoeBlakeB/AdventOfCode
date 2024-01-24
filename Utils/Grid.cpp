// Copyright (C) 2024 Joe Baker (JoeBlakeB)

#include <iterator>
#include <vector>

using namespace std;

enum Direction { UP = 0, RIGHT = 1, DOWN = 2, LEFT = 3 };

struct Coordinate {
    int x;
    int y;

    bool operator==(const Coordinate& other) const {
        return x == other.x && y == other.y;
    }

    bool operator<(const Coordinate& other) const {
        return x < other.x || (x == other.x && y < other.y);
    }

    Coordinate operator()(Direction direction) const {
        return {x + (direction == RIGHT) - (direction == LEFT),
                y + (direction == DOWN) - (direction == UP)};
    }

    friend ostream& operator<<(ostream& os, const Coordinate& c) {
        os << "(" << c.x << ", " << c.y << ")";
        return os;
    }
};

template<typename T>
class Grid {
protected:
    int _width = 0;
    int _height = 0;
    vector<T> grid;
public:
    Grid(int w, int h) : _width(w), _height(h), grid(w * h) {}
    Grid(int w, int h, const T& value) : _width(w), _height(h), grid(w * h, value) {}

    T &operator()(int x, int y) { return grid[y * _width + x]; }
    T &operator()(Coordinate c) { return grid[c.y * _width + c.x]; }
    T &operator[](Coordinate c) { return grid[c.y * _width + c.x]; }
    const T &operator()(int x, int y) const { return grid[y * _width + x]; }
    const T &operator()(Coordinate c) const { return grid[c.y * _width + c.x]; }
    const T &operator[](Coordinate c) const { return grid[c.y * _width + c.x]; }

    int size() const { return _width * _height; }

    const int& width = _width;
    const int& height = _height;

    typename vector<T>::iterator begin() { return grid.begin(); }
    typename vector<T>::iterator end() { return grid.end(); }

    bool contains(int x, int y) const {
        return x >= 0 && x < _width && y >= 0 && y < _height; }
    bool contains(Coordinate c) const {
        return c.x >= 0 && c.x < _width && c.y >= 0 && c.y < _height; }
};

class CharGrid : public Grid<char> {
public:
    CharGrid(int w, int h) : Grid<char>(w, h) {}
    CharGrid(int w, int h, const char& value) : Grid<char>(w, h, value) {}
    CharGrid(istream &input) : Grid<char>(0, 0) {
        string line;
        getline(input, line);
        _width = line.length();
        do {
            if ((int)line.length() != _width) {
                cout << "Error: Grid width is not consistent" << endl;
                exit(1);
            }
            for (int i = 0; i < _width; i++) {
                grid.push_back(line[i]);
            }
            _height++;
        } while (getline(input, line) && line != "");
    }
};
