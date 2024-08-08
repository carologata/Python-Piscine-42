#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("none")
        return
    print(f"parameters: {len(sys.argv)-1}")
    for element in sys.argv[1:]:
        print(f"{element}: {len(element)}")

main()