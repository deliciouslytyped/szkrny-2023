
# 20140108a Osztályok #3 (racionális számok)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20140108a

from infra import ProblemBase

class DenominatorIsZero(Exception):
    pass

from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

class Rational:
    def __init__(self, a, b):
        if not b:
            raise DenominatorIsZero
        g = gcd(a, b)
        self.a = a // g
        self.b = b // g

    def __repr__(self):
        return f"Rational({self.a}/{self.b})"

    def __add__(self, other):
        l = lcm(self.b, other.b)
        return Rational(self.a * l // self.b + other.a * l // other.b, l)

    def __mul__(self, other):
        return Rational(self.a * other.a, self.b * other.b)

    def __sub__(self, other):
        l = lcm(self.b, other.b)
        return Rational(self.a * l // self.b - other.a * l // other.b, l)

    def __truediv__(self, other):
        return Rational(self.a * other.b, self.b * other.a)


class Problem(ProblemBase):
    def check(self):
        t1 = Rational(2, 4)
        assert(repr(t1) == "Rational(1/2)")
        t2 = Rational(7, 13)
        assert(repr(t2) == "Rational(7/13)")
        assert(repr(((t1 + t2) + (t2 - t1)) / Rational(2, 1) * t1) == repr(t2 * t1))
        excepted = 0
        try:
            Rational(2, 0)
        except DenominatorIsZero:
            excepted = 1
        assert(excepted)

if __name__ == "__main__":
    p = Problem()
    p.check()
