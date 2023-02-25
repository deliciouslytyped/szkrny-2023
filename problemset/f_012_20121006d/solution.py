
# 20121006d Fájlkezelés (megjegyzések eltávolítása) [f6]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121006d

from infra import ProblemBase

from pathlib import Path

class Problem(ProblemBase):
    def run(self):
        with open(Path(__file__).parent.parent / "f_002_20120815b" / "string1.py", "r") as f,\
                open("string1_clean.py", "w") as f2:
            f2.writelines(l+"\n" for l in f.read().splitlines() if not l.lstrip().startswith("#"))

if __name__ == "__main__":
    p = Problem()
    p.check()
