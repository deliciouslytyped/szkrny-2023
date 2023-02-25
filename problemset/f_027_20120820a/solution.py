
# 20120820a Tömb rendezett-e
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120820a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run([1,2,3]))
        assert(not self.run([3,2,1]))

    def run(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

if __name__ == "__main__":
    p = Problem()
    p.check()
