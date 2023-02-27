
# 20180307f AoC2017, Day 8, Part 1 (I Heard You Like Registers)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180307f

from infra import ProblemBase

from collections import defaultdict

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("input.txt", "r") as f:
            ss = [[x.split()[0], x.split()[1], int(x.split()[2]), x.split()[4], x.split()[5], int(x.split()[6])] for x in f.readlines()]
            d = defaultdict(int)
            cond = {
                "!=" : lambda a,b: a != b,
                "==" : lambda a,b: a == b,
                "<=" : lambda a,b: a <= b,
                ">=" : lambda a,b: a >= b,
                ">" : lambda a,b: a > b,
                "<" : lambda a,b: a < b,
                }
            for s in ss:
                if cond[s[4]](d[s[3]], s[5]):
                    if s[1] == "inc":
                        d[s[0]] += s[2]
                    else:
                        d[s[0]] -= s[2]
            return max(d.values())

if __name__ == "__main__":
    p = Problem()
    p.check()
