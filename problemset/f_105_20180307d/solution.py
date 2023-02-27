
# 20180307d AoC2017, Day 6, Part 1 (Memory Reallocation)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180307d

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("input.txt", "r") as f:
            s = [int(x) for x in f.readlines()[0].split("\t")]
            #s = [0, 2, 7, 0]
            stateset = set()
            cnt = 0
            while True:
                m = max(s)
                i = s.index(m)
                blocks = m
                s[i] = 0
                while blocks:
                    i += 1
                    s[i % len(s)] += 1
                    blocks -= 1
                cnt += 1
                if tuple(s) in stateset:
                    break
                stateset |= set([tuple(s)])
            print(cnt)
            return cnt

if __name__ == "__main__":
    p = Problem()
    p.check()
