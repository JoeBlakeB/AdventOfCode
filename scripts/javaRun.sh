#!/bin/bash
#
# A simple bash script to build and run a single java file
# with build cache to only re compile if source file changes
#
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# This program is free software under the GPLv3 license.
#

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "Usage: javaRun.sh filename [programs arguments]"
    echo "filename  The java file you want to run"
    exit 0
fi

if [ -z "$1" ]; then
    echo "Error: filename argument is required."
    exit 1
fi

filename="$1"
buildpath="./build/"
outjar="$buildpath$(basename "$filename" .java)".jar

if [ ! -f "$filename" ]; then
    echo "Error: $filename not found"
    exit 1
fi

mkdir -p "$buildpath/${filename%/*}"

# Check the files hash against last time it was built

currentHash=$(sha256sum "$filename")

if [ -f "$buildpath$filename".txt ] && [ -f $outjar ]; then
    previousHash=$(cat "$buildpath$filename".txt)
fi

# If the file has changed

if [ ! "$currentHash" == "$previousHash" ]; then
    # Find the entrypoint of the program

    # Use the filename for unnamed mains
    classname=$(grep -l -E "^public static void main(| )\(String" "$filename" | head -n 1)
    if [ -n "$classname" ]; then
        classname=$(basename "$filename" .java)
    fi

    # If there is a class with the same name as the filename, use that
    if [ -z "$classname" ]; then
        classname=$(grep -E "public class ${filename%.*}" "$filename" | head -n 1 | awk '{print $3}')
    fi

    # If there is no main function, use the first class
    # this wont work, but will give a nicer error message
    if [ -z "$classname" ]; then
        classname=$(grep -E "public class " "$filename" | head -n 1 | awk '{print $3}')
    fi

    if [ -z "$classname" ]; then
        echo "Error: Could not find a class or main function in $filename"
        exit 1
    fi

    # Generate a manifest file with the Main-Class
    manifestFile="$buildpath/manifest.txt"
    echo "Main-Class: $classname" > "$manifestFile"
    
    # Then compile the program
    FAILCMD=javac &&
    javac "$filename" -d "$buildpath$filename" &&
    FAILCMD=jar &&
    jar cfm "$buildpath/$(basename "$filename" .java).jar" "$manifestFile" -C "$buildpath$filename" .

    exitCode=$?
    if [ ! $exitCode -eq 0 ]; then
        echo "Error: $FAILCMD failed to compile $filename"
        if [ -f $outjar ]; then
            rm $outjar
        fi
        exit $exitCode
    fi
    echo -n "$currentHash" > "$buildpath$filename".txt
fi

# And finally, run it

java -jar $outjar "${@:2}"
