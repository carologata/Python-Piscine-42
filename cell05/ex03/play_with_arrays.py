#!/usr/bin/python3

def main() -> None:
    original_array:int = [2, 8, 9, 48, 8, 22, -12, 2]
    new_set = set() 
    for element in original_array:
        if element > 5:
            new_set.add(element + 2)
    print(original_array)
    print(new_set)

main()

