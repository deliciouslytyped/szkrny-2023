
# 20130225a Sztring tisztítása [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130225a

from infra import ProblemBase

import string

class Problem(ProblemBase):
    def check(self):
        assert(self.run("192.20.246.138:\n 6666") == "192.20.246.138:6666")
    def run(self, s):
        return "".join(c for c in s if c not in string.whitespace)

if __name__ == "__main__":
    p = Problem()
    p.check()
