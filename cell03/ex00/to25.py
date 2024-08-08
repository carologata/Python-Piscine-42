#!/usr/bin/python3

def main() -> None:
    try:
        num:int = int(input("Enter a number less than 25\n"))
    except:
        print("Invalid input.")
        return
    if num > 25:
        print("Error")
    else: 
        while num <= 25:
            print(f"Inside the loop, my variable is {num}")
            num += 1

main()