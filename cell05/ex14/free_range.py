#!/usr/bin/python3

import sys

def main() -> None:
    arr = []
    if len(sys.argv) != 3:
        print("none")
        return
    try:
        start:int = int(sys.argv[1])
        end = int(sys.argv[2])
    except:
        print("Invalid input.")   
    for element in range(start, end + 1):
        arr.append(element)
    print(arr)

main()
