
# 20120815f Csinos szám
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815f

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run(1977) == "1,977")
        assert(self.run(2548963) == "2,548,963")
        assert(self.run(-2548963) == "-2,548,963")

    def run(self, n):
        return f"{n:,}"

if __name__ == "__main__":
    p = Problem()
    p.check()
