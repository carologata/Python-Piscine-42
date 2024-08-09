#!/usr/bin/python3

import sys
import re

def main() -> None:
    if len(sys.argv) != 3:
        print("none")
        return
    matches = re.findall(sys.argv[1], sys.argv[2])
    if not matches:
        print("none")
        return
    print(len(matches))

main()