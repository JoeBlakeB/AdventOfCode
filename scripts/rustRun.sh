#!/bin/bash
#
# A simple bash script to build and run a single rust file
# with build cache to only re compile if source file changes
#
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# This program is free software under the GPLv3 license.
#

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "Usage: rustRun.sh filename [programs arguments]"
    echo "filename  The rust file you want to run"
    exit 0
fi

if [ -z "$1" ]; then
    echo "Error: filename argument is required."
    exit 1
fi

filename="$1"
buildpath="./build/"

if [ ! -f "$filename" ]; then
    echo "Error: $filename not found"
    exit 1
fi

mkdir -p "$buildpath/${filename%/*}"

# Check the files hash against last time it was built

currentHash=$(sha256sum "$filename")

if [ -f "$buildpath$filename".txt ] && [ -f "$buildpath$filename" ]; then
    previousHash=$(cat "$buildpath$filename".txt)
fi

# Recompile rust file if needed, then run

if [ ! "$currentHash" == "$previousHash" ]; then
    rustc "$filename" -o "$buildpath$filename"
    exitCode=$?
    if [ ! $exitCode -eq 0 ]; then
        echo "Error: rustc failed to compile $filename"
        if [ -f "$buildpath$filename" ]; then
            rm "$buildpath$filename"
        fi
        exit $exitCode
    fi
    echo -n "$currentHash" > "$buildpath$filename".txt
fi

"$buildpath$filename" "${@:2}"
