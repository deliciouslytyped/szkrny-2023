
# 20180307c AoC2017, Day 5, Part 1 (Maze Runner)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180307c

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("input.txt", "r") as f:
            s = [int(x.strip()) for x in f.readlines()]
            try:
                i, cnt = 0, 0
                while True:
                    j = s[i]
                    s[i] += 1
                    i += j
                    cnt += 1
            except IndexError:
                return cnt

if __name__ == "__main__":
    p = Problem()
    p.check()
