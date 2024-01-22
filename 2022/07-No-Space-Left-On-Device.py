#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 7: No Space Left On Device

with open("inputs/07.txt") as f:
    data = f.read().strip().split("$ ")[1:]

# Get the filesystem

fileList = [{"size": 0, "type": "dir", "children": {}, "name": "/"}]
filesystem = {"/": fileList[0]}
currentPath = []

for row in data:
    command = row[:2]
    if command == "cd":
        cd = row[3:].split("\n")[0]
        if cd == "..":
            currentPath.pop()
        else:
            currentPath.append(cd)
        currentDirectory = filesystem
        for path in currentPath:
            currentDirectory = currentDirectory[path]["children"]
    if command == "ls":
        files = row[3:].strip().split("\n")
        for file in files:
            if file[:3] == "dir":
                fileList.append({"size": 0, "type": "dir", "children": {}, "name": file[4:]})
                currentDirectory[file[4:]] = fileList[-1]
            else:
                fileList.append({"size": int(file.split(" ")[0]), "type": "file", "name": file.split(" ")[1]})
                currentDirectory[file.split(" ")[1]] = fileList[-1]

                updateDirectory = filesystem
                for path in currentPath:
                    updateDirectory[path]["size"] += int(file.split(" ")[0])
                    updateDirectory = updateDirectory[path]["children"]

# Get the total size of all directories at most 100KB

totalSize = 0
for item in fileList:
    if item["type"] == "dir" and item["size"] <= 100000:
        totalSize += item["size"]

print("Total size of all directories at most 100KB:", totalSize)

# Get the smallest directory that will free enough space if deleted

filesystemUsed = filesystem["/"]["size"]
filesystemTotal = 70000000
filesystemFree = filesystemTotal - filesystemUsed
filesystemNeeded = 30000000
filesystemMinimumNeeded = filesystemNeeded - filesystemFree

smallestDirectoryCanDelete = None
smallestDirectorySize = filesystemUsed

for item in fileList:
    if item["type"] == "dir" and item["size"] <= filesystemFree:
        if item["size"] >= filesystemMinimumNeeded and item["size"] < smallestDirectorySize:
            smallestDirectoryCanDelete = item["name"]
            smallestDirectorySize = item["size"]

print(f"The smallest directory that can be deleted is {smallestDirectoryCanDelete} with a size of: {smallestDirectorySize}")