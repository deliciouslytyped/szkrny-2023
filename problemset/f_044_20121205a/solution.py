
# 20121205a sztring karaktereinek az összekeverése
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121205a

from infra import ProblemBase

from random import shuffle
from collections import Counter

class Problem(ProblemBase):
    def check(self):
        s = "Python programming"
        res = self.run(s)
        assert(Counter(res) == Counter(s) and res != s)

    def run(self, a):
        l = list(a)
        shuffle(l)  # or use sample as descrbed in the docs
        return "".join(l)

if __name__ == "__main__":
    p = Problem()
    p.check()
