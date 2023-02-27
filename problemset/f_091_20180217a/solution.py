
# 20180217a lista elemeinek összege / szorzata
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180217a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.rec_sum([1,2,3,4,5,6]) == 21)
        assert(self.rec_prod([1,2,3,4,5,6]) == 720)

    def rec_sum(self, l):
        if not l:
            return 0
        return l[0] + self.rec_sum(l[1:])

    def rec_prod(self, l):
        if not l:
            return 1
        return l[0] * self.rec_prod(l[1:])

if __name__ == "__main__":
    p = Problem()
    p.check()
