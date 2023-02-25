
# 20120815j Egész szám megfordítása [f2]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815j

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run(1977) == 7791)
        assert(self.run(12568) == 86521)

    def run(self, x):
        return int("".join(tuple(reversed(str(x)))))

if __name__ == "__main__":
    p = Problem()
    p.check()
