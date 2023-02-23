
# 20130917a Olvass el!
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130917a

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        return 2**8

if __name__ == "__main__":
    p = Problem()
    p.check()
