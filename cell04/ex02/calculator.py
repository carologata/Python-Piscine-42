#!/usr/bin/python3

def main() -> None:
    try:
        first_number:int = int(input("Give me the first number: "))
        second_number:int = int(input("Give me the second number: "))
    except:
        print("Invalid input.")
        return
    print("Thank you!")
    #Addition
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
    #Subtraction
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
    #Division
    result = first_number // second_number
    print(f"{first_number} / {second_number} = {result}")
    #Multiplication
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")

main()
