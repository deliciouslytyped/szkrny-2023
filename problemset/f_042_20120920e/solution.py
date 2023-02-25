
# 20120920e Sortörés [f4]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120920e

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        import sys
        import random as r

        UPTO = 100

        def main():
            for i in range(UPTO):
                print(r.randint(0, 9), end="")
                if not (i+1) % 10:
                    print()
        main()

if __name__ == "__main__":
    p = Problem()
    p.check()
