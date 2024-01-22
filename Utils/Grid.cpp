// Copyright (C) 2024 Joe Baker (JoeBlakeB)

#include <vector>

using namespace std;

struct Coordinate {
    int x;
    int y;

    bool operator==(const Coordinate& other) const {
        return x == other.x && y == other.y;
    }

    bool operator<(const Coordinate& other) const {
        return x < other.x || (x == other.x && y < other.y);
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
};
