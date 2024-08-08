#!/usr/bin/python3

def main() -> None:
    first_number:int = int(input("Enter the first number:\n"))
    second_number:int = int(input("Enter the second number:\n"))
    result:int = first_number * second_number
    print(first_number, "x", second_number, "=", result)
    if result > 0:
        print("The result is positive")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative") 

main()