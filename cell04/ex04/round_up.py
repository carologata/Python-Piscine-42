#!/usr/bin/python3

import math

def main() -> None:
    try:
        num:int = math.ceil(float(input("Give me a number: ")))
    except:
        print("Not a valid number")
        return
    print(num)

main()