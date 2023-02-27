
# 20171030a bűvös spirál
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20171030a

from infra import ProblemBase

from textwrap import dedent

class Problem(ProblemBase):
    def check(self):
        assert(self.disp(5) == dedent("""
            x1  2  3  4  5 
            16 17 18 19  6 
            15 24 25 20  7 
            14 23 22 21  8 
            13 12 11 10  9 """).lstrip().replace("x", " "))
        assert(self.disp(4) == dedent("""
            x1  2  3  4 
            12 13 14  5 
            11 16 15  6 
            10  9  8  7 """).lstrip().replace("x", " "))
        assert(self.disp(3) == dedent("""
            x1  2  3 
             8  9  4 
             7  6  5 """).lstrip().replace("x", " "))
        assert(self.disp(2) == dedent("""
            x1  2 
             4  3 """).lstrip().replace("x", " "))

    def disp(self, n):
        return "\n".join(("{:^3}"*n).format(*line) for line in self.run(n,1))


    def run(self, w, i):
        if w == 0:
            return []
        if w == 1:
            return [[i]]

        result = [[0 for _ in range(w)] for _ in range(w)]

        # Édes istenem
        result[0] = list(range(i, i+w))
        inner = self.run(w - 2, i + 2 * w + (w - 2) + (w - 2))
        for j in range(1, w-1):
            result[j][1:w-1] = inner[j-1]
        result[-1] = list(range((i-1)+w + (w-2) + w, (i-1)+w + (w-2), -1))

        transpose = [*map(list, zip(*result))]
        transpose[0][1:-1] = list(range((i-1)+4*w-4, (i-1)+3*w-2, -1))
        transpose[-1][1:-1] = list(range((i-1)+w+1, (i-1)+w+1+w-2+1))
        result = [*map(list, zip(*transpose))]

        return result

if __name__ == "__main__":
    p = Problem()
    p.check()
