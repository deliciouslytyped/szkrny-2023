
# 20120820b Decimális → bináris konverter [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120820b

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run(1) == "1")
        assert(self.run(2) == "10")
        assert(self.run(156) == "10011100")
    def run(self, x):
        l = list()
        while x > 0:
            l.append(str(x % 2))
            x //= 2
        return "".join(reversed(l))

if __name__ == "__main__":
    p = Problem()
    p.check()
