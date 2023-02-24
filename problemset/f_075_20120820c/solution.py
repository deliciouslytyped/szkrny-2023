
# 20120820c Első ezer számjegy
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120820c

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        #(9 * 1 + 90 * 2 + x * 3) = 1000
        # x = 270
        r = "".join([str(100+267), str(100+268), str(100+269), str(3)])
        return r

if __name__ == "__main__":
    p = Problem()
    p.check()
