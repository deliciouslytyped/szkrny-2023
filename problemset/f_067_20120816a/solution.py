
# 20120816a 8 királynő [f5]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120816a

from infra import ProblemBase

from textwrap import dedent

class Problem(ProblemBase):
    def check(self):
        assert(self.run([7,3,0,2,5,1,6,4]) == dedent("""
            +-----------------+
            | Q . . . . . . . |
            | . . . . . . Q . |
            | . . . . Q . . . |
            | . . . . . . . Q |
            | . Q . . . . . . |
            | . . . Q . . . . |
            | . . . . . Q . . |
            | . . Q . . . . . |
            +-----------------+""").lstrip())
        assert(self.run([0,4,7,5,2,6,1,3]) == dedent("""
            +-----------------+
            | . . Q . . . . . |
            | . . . . . Q . . |
            | . . . Q . . . . |
            | . Q . . . . . . |
            | . . . . . . . Q |
            | . . . . Q . . . |
            | . . . . . . Q . |
            | Q . . . . . . . |
            +-----------------+""").lstrip())

    def run(self, lst):
        bar = "+-----------------+"
        l = sorted(enumerate([7-x for x in lst]), key=lambda v: v[1])
        r = list()
        r.append(bar)
        for v, _ in l:
            r.append("|" + " ." * v + " Q" + " ." * (7 - v) + " |")
        r.append(bar)
        rr = "\n".join(r)
        print(rr)
        return rr

if __name__ == "__main__":
    p = Problem()
    p.check()
