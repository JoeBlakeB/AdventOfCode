// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 9: Disk Fragmenter
// Usage:
//     scripts/cppRun.sh 2024/09-Disk-Fragmenter.cpp < 2024/inputs/09.txt

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<short> getDisk() {
    vector<short> disk;
    string input;
    getline(cin, input);

    int diskSize = 0;
    for (char c : input) {
        diskSize += c - '0';
    }
    disk.reserve(diskSize);

    int fileCounter = 0;
    bool isFile = true;
    for (char c : input) {
        if (isFile) {
            disk.insert(disk.end(), c - '0', fileCounter);
            fileCounter++;
        } else {
            disk.insert(disk.end(), c - '0', -1);
        }
        isFile = !isFile;
    }

    return disk;
}

vector<short> fragment(vector<short> disk) {
    size_t oldPos = disk.size() - 1;
    size_t newPos = 0;

    while (true) {
        while (newPos < disk.size() && disk[newPos] != -1) {
            newPos++;
        }
        
        while (oldPos > 0 && disk[oldPos] == -1) {
            oldPos--;
        }

        if (newPos >= oldPos) {
            break;
        }
        
        disk[newPos] = disk[oldPos];
        disk[oldPos] = -1;
    }

    return disk;
}

vector<short> defragment(vector<short> disk) {
    int oldPos = disk.size() - 1;
    for (; (oldPos > 0 && disk[oldPos] != -1); oldPos--) {
        break;
    }
    int fileCounter = disk[oldPos];
    int fileLength = 1;
    
    while (fileCounter > 0) {
        while (disk[oldPos-1] > fileCounter || disk[oldPos-1] == -1) {
            oldPos--;
        }
        while (disk[oldPos-1] == fileCounter) {
            fileLength++;
            oldPos--;
        }

        int newPos = 0;
        while (newPos < oldPos) {
            if (disk[newPos] != -1) {
                newPos++;
            } else {
                int gapLength = 1;
                for (; gapLength < fileLength; gapLength++) {
                    if (disk[newPos+gapLength] != -1) {
                        break;
                    }
                }
                if (gapLength == fileLength) {
                    break;
                } else {
                    newPos += gapLength + 1;
                }
            }
        }

        if (newPos < oldPos) {
            for (int i = 0; i < fileLength; i++) {
                disk[newPos+i] = disk[oldPos+i];
                disk[oldPos+i] = -1;
            }
            
        }

        fileCounter--;
        fileLength = 0;
    }

    return disk;
}

long long calculateChecksum(const vector<short>& disk) {
    long long checksum = 0;
    for (size_t i = 0; i < disk.size(); i++) {
        if (disk[i] != -1) {
            checksum += i * disk[i];
        }
    }
    return checksum;
}

int main() {
    vector<short> disk = getDisk();
    cout << "Fragmented Checksum: " << calculateChecksum(fragment(disk)) << endl;
    cout << "Defragmented Checksum: " << calculateChecksum(defragment(disk)) << endl;

    return 0;
}
