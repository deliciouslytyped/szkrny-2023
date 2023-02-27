
# 20121204b ábécésorrendben legnagyobb szó
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121204b

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        with open("words.txt", "r") as f:
            return list(sorted(sum([l.split() for l in f.readlines()], [])))[-1]

if __name__ == "__main__":
    p = Problem()
    p.check()
