
# 20120818f Négyzetek összege, összeg négyzete (PE #6) [f4]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818f

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def closedFormSumOfSquares(self, n):
        return n * (n + 1) * (2 * n + 1) // 6  # TODO safe integer division??

    def run(self):
        sumofhundred = 5050  # as we know by Gauss
        return sumofhundred**2 - self.closedFormSumOfSquares(100)

if __name__ == "__main__":
    p = Problem()
    p.check()
