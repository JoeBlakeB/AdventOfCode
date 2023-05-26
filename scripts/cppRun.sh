#!/bin/bash
#
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# This program is free software under the GPLv3 license.
#

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "Usage: cppRun.sh filename [programs arguments]"
    echo "filename  The c++ file you want to run"
    exit 0
fi

if [ -z "$1" ]; then
    echo "Error: filename argument is required."
    exit 1
fi

filename="$1"
compiledname="${filename%.*}"
buildpath="./build/"

if [ ! -f "$filename" ]; then
    echo "Error: $filename not found"
    exit 1
fi

mkdir -p "$buildpath/${filename%/*}"

# Check the files hash against last time it was built

currentHash=$(sha256sum "$filename")

if [ -f "$buildpath$filename".txt ] && [ -f "$buildpath$compiledname" ]; then
    previousHash=$(cat "$buildpath$filename".txt)
fi

# Recompile c++ file if needed, then run

if [ ! "$currentHash" == "$previousHash" ]; then
    g++ -std=c++17 -Wall -Wextra -Wpedantic -O3 -lssl -lcrypto -o "$buildpath$compiledname" "$filename"

    exitCode=$?
    if [ ! $exitCode -eq 0 ]; then
        echo "Error: g++ failed to compile $filename"
        if [ -f "$buildpath$compiledname" ]; then
            rm "$buildpath$compiledname"
        fi
        exit $exitCode
    fi
    echo -n "$currentHash" > "$buildpath$filename".txt
fi

"$buildpath$compiledname" "${@:2}"
