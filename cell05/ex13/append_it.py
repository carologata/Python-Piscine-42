#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("none")
        return
    for element in sys.argv[1:]:
        if not element.endswith("ism"):
            print(f"{element}ism")

main()