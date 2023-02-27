
# 20190406a Egyedi azonosítók generálása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20190406a

import csv
import string

if __name__ == "__main__":

    with open("output.csv", "w", newline='') as csvfile:
        w = csv.writer(csvfile)
        max = 26 * 1000 + 999
        for i, (nev, neptun) in enumerate(csv.reader(open("input.csv", "r"))):
            assert(i < max)
            i1 = string.ascii_uppercase[i // 1000]
            i2 = i % 1000
            w.writerow([nev, f"{i1}-{i2:03}"])
