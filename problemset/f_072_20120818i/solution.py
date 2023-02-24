
# 20120818i Számjegyek összege (PE #16)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818i

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        return sum([int(x) for x in str(2**1000)])

if __name__ == "__main__":
    p = Problem()
    p.check()
