#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("none")
        return
    print(sys.argv[1].lower())

main()
