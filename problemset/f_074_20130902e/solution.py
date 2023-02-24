
# 20130902e Zárójelek (*)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130902e

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run("((5+3)*2+1)") == True)
        assert(self.run("{[(3+1)+2]+}") == True)
        assert(self.run("(3+{1-1)}") == False)
        assert(self.run("[1+1]+(2*2)-{3/3}") == True)
        assert(self.run("(({[(((1)-2)+3)-3]/3}-3)") == False)

    def run(self, expr):
        l = list()
        sym = {"(": ")", "[": "]", "{": "}"}
        for c in expr:
            if c in "[{(":
                l.append(c)
            elif c in "]})":
                r = l.pop()
                if c != sym[r]:
                    return False
        return l == []


if __name__ == "__main__":
    p = Problem()
    p.check()
