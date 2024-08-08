#!/usr/bin/python3

import sys

def main() -> None:
    
    if len(sys.argv) < 3:
        print("none")
        return
    
    # sys.argv[1:]: This returns a new list containing all the command-line arguments except the first one (which is the script name).
    # reversed() is used to iterate over the arguments in reverse order, eliminating the need for a while loop and manual decrementing.
    for element in reversed(sys.argv[1:]): 
        print(element)

main()