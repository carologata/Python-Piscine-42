#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("none")
        return
    for char in sys.argv[1]:
        if char == 'z':
            print(char, end="")
    print()

main()
