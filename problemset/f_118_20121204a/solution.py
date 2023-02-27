
# 20121204a két file összefésülése
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121204a

if __name__ == "__main__":
    with open("f1.txt", "r") as f1, open("f2.txt", "r") as f2:
        for i in sorted([int(x.strip()) for x in f1.readlines()] + [int(x.strip()) for x in f2.readlines()]):
            print(i)
