
# 20130902d Prím palindróm
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130902d

from infra import ProblemBase
from math import sqrt

class Problem(ProblemBase):
    def check(self):
        assert(self.run(31) == 101)
        assert(self.run(130) == 131)
        assert(self.run(131) == 131)
        assert(self.run(1977) == 10301)

    def run(self, x):
        def isprime(x):
            lim = int(sqrt(x))
            for i in range(2, lim+1):
                if x % i == 0:
                    return False
            return True

        def ispalindrome(x):
            return str(x) == str(x)[::-1]

        while not ispalindrome(x) or not isprime(x):
            x+=1
        return x

if __name__ == "__main__":
    p = Problem()
    p.check()
