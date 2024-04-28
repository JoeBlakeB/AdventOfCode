#!/bin/bash
#
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
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

# Get a list of all files to check for changes that are included in the c++ file

files=$(grep -oP '#include\s*"\K[^"]*' "$filename" |
        sed "s|^|${filename%/*}\/|")

# Check all files hashes against last time it was built

currentHashes=$(printf "$filename\n$files" | tr '\n' '\0' | xargs -0 sha256sum)

if [ -f "$buildpath$filename".txt ] && [ -f "$buildpath$compiledname" ]; then
    previousHashes=$(cat "$buildpath$filename".txt)
fi

# Recompile c++ file if needed, then run

if [ ! "$currentHashes" == "$previousHashes" ]; then

    # Only include ssl and crypto if required
    
    if grep -q "#include <openssl" "$filename"; then
        openssl="-lssl -lcrypto"
    fi

    # Compile

    g++ -std=c++23 -Wall -Wextra -Wpedantic -O3 $openssl -o "$buildpath$compiledname" "$filename"

    exitCode=$?
    if [ ! $exitCode -eq 0 ]; then
        echo "Error: g++ failed to compile $filename"
        if [ -f "$buildpath$compiledname" ]; then
            rm "$buildpath$compiledname"
        fi
        exit $exitCode
    fi
    echo -n "$currentHashes" > "$buildpath$filename".txt
fi

"$buildpath$compiledname" "${@:2}"
