#!/usr/bin/python3

def main() -> None:
    original_array:int = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []
    for element in original_array:
        if element > 5:
            new_array.append(element + 2)
    print(original_array)
    print(new_array)

main()

# def main() -> None:
#     original_array:int = [2, 8, 9, 48, 8, 22, -12, 2]
#     new_array = []
#     for element in range(0, len(original_array)):
#         if original_array[element] > 5:
#             new_array.append(original_array[element] + 2)
#     print(original_array)
#     print(new_array)
