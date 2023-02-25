
# 20120905c My shuffle (shuffled) [f8]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120905c

from infra import ProblemBase

from random import shuffle

class Problem(ProblemBase):
    def check(self):
        l = [1,2,3,4,5,6,71]
        r = self.run(l)
        assert(r[-1] in l and r != l)

    def run(self, l):
        def shuffled(l):
            l = list(l)
            shuffle(l)
            return l
        return shuffled(l)


if __name__ == "__main__":
    p = Problem()
    p.check()
