#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("none")
    else:
        print(sys.argv[1].upper())

main()
