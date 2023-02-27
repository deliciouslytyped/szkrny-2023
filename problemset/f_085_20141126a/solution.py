
# 20141126a palindróm két számrendszerben is (PE #36)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20141126a

from infra import ProblemBase

class Problem(ProblemBase):
    has_check = True
    def run(self):
        return sum(i for i in range(1_000_000) if tuple(bin(i)[2:]) == tuple(reversed(bin(i)[2:])) and tuple(str(i)) == tuple(reversed(str(i))))


if __name__ == "__main__":
    p = Problem()
    p.check()
