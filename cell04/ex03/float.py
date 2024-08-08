#!/usr/bin/python3

def main() -> None:
    num:float = float(input("Give me a number: "))
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

main()