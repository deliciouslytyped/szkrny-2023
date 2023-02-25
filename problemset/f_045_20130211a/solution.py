
# 20130211a anagramma [f6]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130211a

from infra import ProblemBase

from collections import Counter
from itertools import permutations

class Problem(ProblemBase):
    def check(self):
        assert(self.run("listen", "silent"))
        assert(self.run("A gentleman", "Elegant man"))
        assert(self.run("Clint Eastwood", "Old west action"))
        assert(self.run("dormitory", "dirty room"))
        assert(self.alternative("listen", "silent"))
        assert(self.alternative("A gentleman", "Elegant man"))
        assert(self.alternative("Clint Eastwood", "Old west action"))
        assert(self.alternative("dormitory", "dirty room"))

    def alternative(self, a, b):  # This is of course a terribly non-performant solution
        norm = lambda x: x.lower().replace(" ", "")
        return tuple(norm(b)) in permutations(norm(a))

    def run(self, a, b):
        norm = lambda x: x.lower().replace(" ", "")
        return Counter(norm(a)) == Counter(norm(b))

if __name__ == "__main__":
    p = Problem()
    p.check()
