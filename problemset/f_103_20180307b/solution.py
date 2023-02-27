
# 20180307b AoC2017, Day 4, Part 1 (High-Entropy Passphrases)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180307b

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("input.txt", "r") as f:
            s = f.readlines()
            return sum(1 for x in s if not len(set(x.split())) < len(x.split()))

if __name__ == "__main__":
    p = Problem()
    p.check()
