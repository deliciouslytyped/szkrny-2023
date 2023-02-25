
# 20120818e Ezernél kisebb pozitív egész számok (PE #1) [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818e

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        return sum(x for x in range(1000) if not x % 5 or not x % 3)

if __name__ == "__main__":
    p = Problem()
    p.check()
