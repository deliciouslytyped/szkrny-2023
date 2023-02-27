
# 20130305a XOR [f4]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130305a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.myxor(True, True) == False)
        assert(self.myxor(False, False) == False)
        assert(self.myxor(True, False) == True)
        assert(self.myxor(False, True) == True)
        assert(self.myxor([], []) == False)
        assert(self.myxor([1,2,3], []) == True)

    def myxor(self, a, b):
        return bool(a) ^ bool(b)

if __name__ == "__main__":
    p = Problem()
    p.check()
