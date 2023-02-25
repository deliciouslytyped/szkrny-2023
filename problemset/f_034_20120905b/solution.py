
# 20120905b Lista elemeinek szorzata [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120905b

from infra import ProblemBase

from math import prod

class Problem(ProblemBase):
    def run(self, l):
        return prod(l)

if __name__ == "__main__":
    p = Problem()
    p.check()
