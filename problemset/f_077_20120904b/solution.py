
# 20120904b Lista egy részének a megfordítása [f10]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120904b

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run([1, 2, 9, 6, 5], 2, 4) == [1, 2, 5, 6, 9])

    def run(self, l, a, b):
        return l[:a] + list(reversed(l[a:b+1])) + l[b+1:]

if __name__ == "__main__":
    p = Problem()
    p.check()
