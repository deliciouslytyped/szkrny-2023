
# 20170314a π értékének meghatározása random számokkal
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20170314a

from infra import ProblemBase

from random import randint
from math import gcd,sqrt

class Problem(ProblemBase):
    def run(self):
        nmax = 500
        a, b = 1, 120
        coprime = 0

        for i in range(nmax):
            c, d = randint(a, b), randint(a, b)
            coprime += (gcd(c, d) == 1)

        print(sqrt(6.0/(coprime/nmax)))

if __name__ == "__main__":
    p = Problem()
    p.check()
