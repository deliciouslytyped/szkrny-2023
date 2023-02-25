
# 20121001b Egész számok összege 1-től 100-ig [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121001b

from infra import ProblemBase


# TODO the single instance of multiple checked subproblems and I don't feel like updating the code to handle it right now
class Problem(ProblemBase):
    def run(self):
        print(sum(sum([[int(y) for y in str(x)] for x in range(1, 100+1)], [])))

if __name__ == "__main__":
    p = Problem()
    p.check()
