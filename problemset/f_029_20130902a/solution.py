
# 20130902a Medián
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130902a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run([1, 2, 3, 4, 5]) == 3)
        assert(self.run([3, 1, 2, 5, 3]) == 3)
        assert(self.run([1, 300, 2, 200, 1]) == 2)
        assert(self.run([3, 6, 20, 99, 10, 15]) == 12.5)

    def run(self, l):  # statistics.median though
        l.sort()
        mid = len(l)//2
        return (l[mid] + l[~mid]) / 2  # finally found how to do this variant https://stackoverflow.com/a/48369590

if __name__ == "__main__":
    p = Problem()
    p.check()
