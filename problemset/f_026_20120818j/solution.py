
# 20120818j Számjegyek száma [f2]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818j

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        return len(str(2**256))

if __name__ == "__main__":
    p = Problem()
    p.check()
