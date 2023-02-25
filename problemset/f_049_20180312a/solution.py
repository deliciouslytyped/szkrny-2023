
# 20180312a zipper
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180312a

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        chars = "abcdefghijklmnopqrstuvwxyz"
        codes = list(range(ord('a'), ord('z')+1))

        for t in zip(chars, codes):
            print(t)

if __name__ == "__main__":
    p = Problem()
    p.check()
