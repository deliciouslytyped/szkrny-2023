
# 20190901a Fizz Buzz
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20190901a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run(16) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz", 16])

    def run(self, n):
        r = list()
        for i in range(1, n+1):
            if not i % 3 and not i % 5:
                r.append("fizzbuzz")
            elif not i % 3:
                r.append("fizz")
            elif not i % 5:
                r.append("buzz")
            else:
                r.append(i)
        print(r)
        return r

if __name__ == "__main__":
    p = Problem()
    p.check()
