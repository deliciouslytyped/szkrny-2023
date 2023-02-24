
# 20120815i Fibonacci számok
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815i

from infra import ProblemBase

class Problem(ProblemBase):
    def simple_fib(self, n):
        l = [0, 1]
        def fib(a,b):
            return a + b
        for i in range(2,n+1):
            l.append(fib(l[i-1], l[i-2]))
        return l

    def check(self):
        val = self.run()
        print(val)
        assert(val == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def run(self):
        return self.simple_fib(10)

if __name__ == "__main__":
    p = Problem()
    p.check()
