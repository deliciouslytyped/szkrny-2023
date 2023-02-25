
# 20120904a Duplikátumok eltávolítása (halmaz01) [f5]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120904a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        l = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
        assert(self.run(l) == [-200, 1, 2, 3, 4, 5])

    def run(self, l):
        return list(sorted(set(l)))

if __name__ == "__main__":
    p = Problem()
    p.check()
