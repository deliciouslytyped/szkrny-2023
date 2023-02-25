
# 20130902b Hamming-távolság (*)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130902b

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run("toned", "roses") == 3)

    def run(self, a, b):
        if len(a) != len(b):
            raise ValueError
        return sum(x != y for x, y in zip(a, b))

if __name__ == "__main__":
    p = Problem()
    p.check()
