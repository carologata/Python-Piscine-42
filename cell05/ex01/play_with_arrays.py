#!/usr/bin/python3

def main() -> None:
    original_array:int = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []
    for element in range(0, len(original_array)):
        new_array.append(original_array[element] + 2)
    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")

main()