
# 20120815d ASCII táblázat [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815d

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        for i in range(32, 127+1):
            c = chr(i)
            print(f"{i}: {c}")
        return sum(range(ord('A'), ord('Z')+1))

if __name__ == "__main__":
    p = Problem()
    p.check()
