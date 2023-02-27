#!/usr/bin/env python3

import sys

def main():
    with open("flipz.py", "r") as f, open("flipped.py","w") as f2:
        f2.write(f.read()[::-1])

##############################################################

if __name__ == "__main__":
    main()