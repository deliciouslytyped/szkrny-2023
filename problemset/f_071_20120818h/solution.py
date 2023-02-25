
# 20120818h 100 db 50-jegyű szám (PE #13) [f5][f6]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818h

from infra import ProblemBase

from pathlib import Path

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open(Path(__file__).parent / "data.txt", "r") as f:
            return str(sum(int(x) for x in f.readlines()))[:10]

if __name__ == "__main__":
    p = Problem()
    p.check()
