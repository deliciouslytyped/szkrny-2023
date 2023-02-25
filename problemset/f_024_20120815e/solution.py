
# 20120815e Palindróm [f2]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815e

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        s = "amanaplanacanalpanama"
        assert(self.triv(s))
        assert(self.itera(s))
        assert(self.recu(s))

    def triv(self, s):
        return tuple(reversed(s)) == tuple(s)

    def itera(self, s):
        return all(s[i] == s[~i] for i in range(len(s)//2))

    def recu(self, s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and self.recu(s[1:-1])

if __name__ == "__main__":
    p = Problem()
    p.check()
