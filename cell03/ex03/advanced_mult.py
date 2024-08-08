#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) > 1:
        print("none")
        return
    i = 0
    while i <= 10:
        j = 0
        print(f"Table de {i}:", end="")
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
        print("")
        i += 1

main()