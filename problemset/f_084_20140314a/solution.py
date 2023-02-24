
# 20140314a nyomtatandó oldalak
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20140314a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        print(self.run("1-4,7,9,11-15"))
        assert(self.run("1-4,7,9,11-15") == [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15])
        assert(self.run("7") == [7])

    def run(self, expr):
        rangeexpr = lambda x: list(range(int(x[0]), int(x[1]) + 1))
        return sum( [(rangeexpr(x.split("-")) if "-" in x else [int(x)]) for x in expr.split(",")], [])

if __name__ == "__main__":
    p = Problem()
    p.check()
