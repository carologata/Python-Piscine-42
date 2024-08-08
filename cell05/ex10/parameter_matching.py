#!/usr/bin/python3

import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("none")
        return
    answer:str = input("What was the parameter? ")
    if answer == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()