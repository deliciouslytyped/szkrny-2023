
# 20180217b xn
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180217b

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.nthpow(3, 10) == 3 ** 10)

    def nthpow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.nthpow(x, -n)
        if n % 2:  # odd
            return x * self.nthpow(x, n-1)
        else:
            y = self.nthpow(x, n//2)
            return y * y

if __name__ == "__main__":
    p = Problem()
    p.check()
