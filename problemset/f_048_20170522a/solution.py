
# 20170522a felhőkarcolók
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20170522a

from infra import ProblemBase

from itertools import tee

# https://docs.python.org/3/library/itertools.html#itertools.pairwise
# ended up being too painful to try to upg. to 3.10
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Problem(ProblemBase):
    has_check = True

    def run(self):
        return sum(abs(int(x) - int(y)) for x, y in pairwise(str(2**1024)))

if __name__ == "__main__":
    p = Problem()
    p.check()
