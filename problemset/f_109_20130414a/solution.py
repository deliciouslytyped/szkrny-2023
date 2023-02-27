
# 20130414a password generátor
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130414a

from infra import ProblemBase

from secrets import choice
import string

class Problem(ProblemBase):
    def check(self):
        print(self.run())

    def run(self, n=8):
        return "".join(choice(string.ascii_letters + string.digits) for _ in range(n))

if __name__ == "__main__":
    p = Problem()
    p.check()
