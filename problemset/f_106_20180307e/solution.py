
# 20180307e AoC2017, Day 7, Part 1 (Processes)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180307e

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("input.txt", "r") as f:
            s = [[y.split()[0] if len(y.split()) > 1 and y.split()[1].startswith("(") else y.split(", ") for y in x.strip().split(" -> ")] for x in f.readlines()]
            l = set(x[0] for x in s)
            r = set(sum((x[1] for x in s if len(x) > 1), []))
            return list(l - r)[0]

if __name__ == "__main__":
    p = Problem()
    p.check()
