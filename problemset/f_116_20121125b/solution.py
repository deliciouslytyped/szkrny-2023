
# 20121125b PTI-s hallgatók
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121125b

from infra import ProblemBase

import csv

class Problem(ProblemBase):
    def run(self):
        print(", ".join(sorted(keresztnev.capitalize() for keresztnev, _, szak in csv.reader(open("nevek.csv", "r")) if szak.lower() == "pti")))


if __name__ == "__main__":
    p = Problem()
    p.check()
