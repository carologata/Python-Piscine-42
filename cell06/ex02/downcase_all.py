#!/usr/bin/python3

import sys

def downcase_it(word:str) -> str:
    return word.lower()

def main() -> None:
    if len(sys.argv) < 2:
        print("none")
    for element in sys.argv[1:]:
        print(downcase_it(element))

main()