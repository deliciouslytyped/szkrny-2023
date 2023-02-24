
# 20120831a PI értékének közelítése
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120831a

from infra import ProblemBase

from math import pi

class Problem(ProblemBase):
    def check(self):
        assert(round(self.run(), 5) == round(pi, 5))

    def run(self):
        v = 0
        i = 1
        while abs(pi - 4 * v) > 0.000001:
            v += 1/i
            i = -1 * (i/abs(i)) * (abs(i) + 2)
        return 4 * v

if __name__ == "__main__":
    p = Problem()
    p.check()
