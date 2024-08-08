#!/usr/bin/python3

import sys

def main() -> None:
    number_of_arguments:int = len(sys.argv) - 1
    print(f"Number of parameters: {number_of_arguments}.")

main()