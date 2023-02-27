
# 20180307a AoC2017, Day 2, Part 1 (Corruption Checksum)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180307a

from infra import ProblemBase

from textwrap import dedent

class Problem(ProblemBase):
    has_check = True
    #def check(self):
    #    assert(self.run(dedent("""
    #        5 1 9 5
    #        7 5 3
    #        2 4 6 8""").strip()) == 18)

    def run(self):#,s):
        with open("input.txt", "r") as f:
            s = f.readlines()
            return sum(max(int(x) for x in l.split())-min(int(x) for x in l.split()) for l in s)

if __name__ == "__main__":
    p = Problem()
    p.check()
