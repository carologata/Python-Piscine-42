#!/usr/bin/python3

def main() -> None:
    try:
        num:int = int(input("Enter a number\n"))
    except:
        print("Invalid input.")
        return
    i:int = 0
    while i < 10:
        result:int = num * i
        print(f"{i} x {num} = {result}")
        i += 1

main()