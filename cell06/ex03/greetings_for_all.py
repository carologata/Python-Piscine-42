#!/usr/bin/python3

def is_number(name:str) -> bool:
    try:
        float(name)
        return True
    except:
        return False

def greetings(name:str = "") -> None:
    if not name:
        print("Hello, noble stranger.")
    elif is_number(name):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)