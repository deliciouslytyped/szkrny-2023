
# 20190914a Nagy számok rovatunkban: 42
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20190914a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(42 == (-80538738812075974)**3 + 80435758145817515**3 + 12602123297335631**3)

if __name__ == "__main__":
    p = Problem()
    p.check()
