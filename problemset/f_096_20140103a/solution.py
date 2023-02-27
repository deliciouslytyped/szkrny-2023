
# 20140103a 2022
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20140103a

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        f = lambda x: str(ord(x))
        print(f('')+f(''))

if __name__ == "__main__":
    p = Problem()
    p.check()
