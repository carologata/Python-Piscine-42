#!/usr/bin/python3

def add_one(variable:int) -> None:
    try:
        variable += 1
    except:
        print("Invalid input.")

def main() -> None:
    i = 1
    print(i)
    add_one(i)
    print(i)

main()