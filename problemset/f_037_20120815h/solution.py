
# 20120815h a-z [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815h

from infra import ProblemBase

import string

class Problem(ProblemBase):
    def run(self):
        for i in string.ascii_lowercase:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    p = Problem()
    p.check()
