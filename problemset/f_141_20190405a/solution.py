
# 20190405a Nézőtér
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20190405a

from infra import ProblemBase

from math import floor
from collections import Counter
import re

class Problem(ProblemBase):
    def run(self):
        #print("1.feladat")
        foglaltsag = list()
        kategoria = list()
        with open("foglaltsag.txt", "r") as f, open("kategoria.txt", "r") as k:
            foglaltsag = [x.rstrip() for x in f.readlines()]
            kategoria = [x.rstrip() for x in k.readlines()]

        print("2.feladat")
        sor = int(input("sor szám: "))
        szek = int(input("szek szám: "))
        print("foglalt" if foglaltsag[sor-1][szek-1] == "x" else "szabad")

        print("3.feladat")
        eladott = sum(sum([[1 for y in x if y == "x"] for x in foglaltsag], []))
        ossz = sum(len(x) for x in foglaltsag)
        print( "Az előadásra eddig %s jegyet adtak el, ez a nézőtér %s%%-a." % (eladott, floor(eladott / ossz * 100)) )

        print("4.feladat")
        d = Counter([y for x, y in zip("".join(foglaltsag), "".join(kategoria)) if x == "x"])
        print("A legtöbb jegyet a(z) %s. árkategóriában értékesítették." % next(iter(sorted(d.items(), key=lambda x: x[1])))[0] )

        print("5.feladat")
        ar = [0, 5000, 4000, 3000, 2000, 1500]
        d = sum([ar[int(y)] for x, y in zip("".join(foglaltsag), "".join(kategoria)) if x == "x"])

        print("6.feladat")
        c = 0
        for r in foglaltsag:
            c += len([x for x in range(len(r)-2) if r[x:x+2+1] == "xox"]) + r.startswith("ox") + r.endswith("xo")
        print(f"{c} egyedülálló üres hely van a nézőtéren.")

        #print("7.feladat")
        with open("szabad.txt", "w") as f:
            for rf, rk in zip(foglaltsag, kategoria):
                f.write("".join([x if x == "x" else y for x, y in zip(rf, rk)]) + "\n")


if __name__ == "__main__":
    p = Problem()
    p.check()
