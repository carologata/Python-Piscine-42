#!/usr/bin/python3

def main() -> None:
    value: str = input()
    num: int = int(value)
    if num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")

main()