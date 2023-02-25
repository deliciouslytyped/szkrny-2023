
# 20200801a operátorok
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20200801a

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        allowed = {
            "+" : "__add__",
            "-" : "__sub__",
            "*" : "__mul__",
            "/" : "__div__",
            "%" : "__mod__",
            "^" : "__pow__" }
        a = int(input("1. szám: "))
        o = input("Operátor: ")
        b = int(input("2. szám: "))
        res = getattr(a, allowed[o])(b)
        print(f"Eredmény: {res}")

if __name__ == "__main__":
    p = Problem()
    p.check()
