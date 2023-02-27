
# 20221006a Halmaz megvalósítása szótárral (a "Duplikátumok eltávolítása (halmaz01)" c. feladat variációja)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20221006a

from infra import ProblemBase


class Problem(ProblemBase):
    def check(self):
        l = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
        assert(self.run(l) == [-200, 1, 2, 3, 4, 5])

    def run(self, l):
        d = {}.fromkeys(l)
        return sorted(d.keys())

if __name__ == "__main__":
    p = Problem()
    p.check()
