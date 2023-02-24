
# 20120815g PI vers [f6]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815g

from infra import ProblemBase

import math
from textwrap import dedent
poem = dedent("""
    How I want a drink
    alcoholic of course
    After the heavy lectures
    involving complex functions""")


class Problem(ProblemBase):
    def readable(self):
        words = poem.split()
        digits = str(math.pi).replace(".","")
        equal = [ len(x) == int(y) for x, y in zip(words, digits) ]
        print(all(equal))

    def allinone(self):
        print(all([len(x) == int(y) for x, y in zip(poem.split(), str(math.pi).replace(".", ""))]))

    def run(self):
        self.readable()
        self.allinone()


if __name__ == "__main__":
    p = Problem()
    p.check()
