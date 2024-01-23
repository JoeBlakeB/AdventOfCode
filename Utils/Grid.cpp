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
    vector<T> map;
public:
    Grid(int w, int h) : _width(w), _height(h), map(w * h) {}
    Grid(int w, int h, const T& value) : _width(w), _height(h), map(w * h, value) {}
    
    T& operator()(int x, int y) { return map[y * _width + x]; }
    T& operator()(Coordinate c) { return map[c.y * _width + c.x]; }
    const T& operator()(int x, int y) const { return map[y * _width + x]; }
    const T& operator()(Coordinate c) const { return map[c.y * _width + c.x]; }

    int size() const { return _width * _height; }

    const int& width = _width;
    const int& height = _height;

    typename vector<T>::iterator begin() { return map.begin(); }
    typename vector<T>::iterator end() { return map.end(); }
};
