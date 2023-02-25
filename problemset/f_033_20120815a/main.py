import sys

if __name__ == "__main__":
    sys.argv.extend(("1", "2"))
    print(sys.argv)

    if len(sys.argv) < 3:
        print("Nem adott meg elég argumentumot!")
        sys.exit(1)

    print(int(sys.argv[1]) + int(sys.argv[2]))