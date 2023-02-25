
# 20130218b bizonyos karakterek [f5]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130218b

from infra import ProblemBase

import string

class Problem(ProblemBase):
    def check(self):
        assert(self.run("Barking!") == "B")
        assert(self.run("KL754", "0123456789") == "754")
        assert(self.run("BEAN", "abcdefghijklmnopqrstuvwxyz") == "")

    def run(self, text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
        return "".join(x for x in text if x in chars)

if __name__ == "__main__":
    p = Problem()
    p.check()
