
# 20130902c Mondat extra szóközök nélkül (*)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130902c

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run('I  love   Python') == "I love Python")

    def run(self, s):
        return " ".join(s.split())

if __name__ == "__main__":
    p = Problem()
    p.check()
