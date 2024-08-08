#!/usr/bin/python3

def main() -> None:
    password:str = "Python is awesome"
    attempt:str = input()
    if attempt == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

main()