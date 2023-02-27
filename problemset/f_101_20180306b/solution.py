
# 20180306b AoC2017, Day 1, Part 1 (Inverse Captcha)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180306b

from infra import ProblemBase

from itertools import tee
def pairwise(iterable): # (available in 3.10)
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Problem(ProblemBase):
    has_check = True
    #def check(self):
    #    assert(self.run("1122") == 3)
    #    assert(self.run("1111") == 4)
    #    assert(self.run("1234") == 0)
    #    assert(self.run("91212129") == 9)

    def run(self):#, s):
        with open("input.txt", "r") as f:
            s = f.readlines()[0]
            return sum(int(x) for x, y in pairwise(s+s[0]) if x == y)

if __name__ == "__main__":
    p = Problem()
    p.check()
