#!/usr/bin/python3

# def main() -> None:   
#     new_word:str = ""  
#     word:str = input()
#     for char in word:
#         if char.isupper():
#             new_word += char.lower()
#         else:
#             new_word += char.upper()    
#     print(new_word)

def main() -> None:
    word:str = input().swapcase()
    print(word)

main()