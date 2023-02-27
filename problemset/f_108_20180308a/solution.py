
# 20180308a AoC2017, Day 12, Part 1 (Digital Plumber)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180308a

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("input.txt", "r") as f:
            d = {int(l.split(" <-> ")[0]) : [int(x) for x in l.split(" <-> ")[1].split(", ")] for l in f.readlines()}

        closure = set([0])
        prev = 0
        while len(closure) != prev:
            prev = len(closure)
            closure |= set(sum((d[y] for y in closure), []))
        return len(closure)

if __name__ == "__main__":
    p = Problem()
    p.check()
