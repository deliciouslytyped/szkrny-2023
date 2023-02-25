
# 20210424a Az ABACABA sorozat
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20210424a

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        x = 1
        i = 1
        while i < 26:
            i += 1
            x = 2 * x + 1
        return x

if __name__ == "__main__":
    p = Problem()
    p.check()
