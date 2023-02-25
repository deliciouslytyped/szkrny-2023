
# 20120920c Hány naposak vagyunk?
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120920c

from infra import ProblemBase

from datetime import date

class Problem(ProblemBase):
    def run(self):
        date.today() - date(1980,1,1)

if __name__ == "__main__":
    p = Problem()
    p.check()
