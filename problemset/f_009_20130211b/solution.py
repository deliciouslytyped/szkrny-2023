
# 20130211b Diamond (ciklus) [f4]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130211b

from infra import ProblemBase

from textwrap import dedent

class Problem(ProblemBase):
    def check(self):
        assert(self.run(3) == dedent("""    
            x*
            ***
             *
            """).lstrip().replace("x", " "))
        assert(self.run(7) == dedent("""    
            xxx*
              ***
             *****
            *******
             *****
              ***
               *
            """).lstrip().replace("x", " "))

    def run(self, n):
        acc = ""

        if not n % 2:
            print(f"Csak paros méretű lehet a gyémánt! Az n={n} nem páros.")
            return

        for i in range(n//2):
            acc += ("*"*(2*i+1)).center(n).rstrip() + "\n"
        acc += "*"*n + "\n"
        for i in range(n//2-1, 0-1, -1):
            acc += ("*"*(2*i+1)).center(n).rstrip() + "\n"

        print(acc)
        return acc
if __name__ == "__main__":
    p = Problem()
    p.check()
