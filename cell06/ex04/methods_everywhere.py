#!/usr/bin/python3

import sys

def shrink(word:str) -> None:
    try:
        slices = slice(0, 8) 
        print(word[slices])
    except:
        print("Invalid input.")

def enlarge(word:str) -> None:
    try:
        word_len = len(word)
        print(word, end="")
        while word_len < 9:
            print('Z', end="")
            word_len += 1
        print()
    except:
        print("Invalid input.") 


def main() -> None:
    if len(sys.argv) < 2:
        print("none")
        return
    for word in sys.argv[1:]:
        word_len = len(word)
        if word_len > 8:
            shrink(word)
        elif word_len < 8:
            enlarge(word)
        else:
            print(word)

main()