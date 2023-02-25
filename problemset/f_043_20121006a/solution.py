
# 20121006a kis- és nagybetűs ábécé
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121006a

from infra import ProblemBase

import string

class Problem(ProblemBase):
    def check(self):
        assert(self.run() == "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB")

    def run(self):
        rot2 = lambda x: [x[(i + 2) % len(x)] for i in range(len(x))]
        return "".join(rot2(string.ascii_lowercase) + rot2(string.ascii_uppercase))

if __name__ == "__main__":
    p = Problem()
    p.check()
