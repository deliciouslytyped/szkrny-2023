
# 20141125a Osztályok #1 verem és sor megvalósítása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20141125a

from infra import ProblemBase


class Verem:
    def __init__(self):
        self.stack = list()

    def betesz(self, e):
        self.stack.append(e)

    def kivesz(self):
        try: # This is what our spec requires...
            return self.stack.pop()
        except IndexError:
            return None

    def meret(self):
        return len(self.stack)

    def ures(self):
        return not bool(self.stack)

    def __repr__(self):
        return "[" + " ".join(repr(x) for x in self.stack)

class Sor:
    def __init__(self):
        self.stack = list()
        self.consumed = 0

    def __repr__(self):
        return "[" + " ".join(repr(x) for x in self.stack[self.consumed:])

    def hozzaad(self, e):
        self.stack.append(e)

    def kivesz(self):
        r = self.stack[self.consumed]
        self.consumed += 1
        return r

    def meret(self):
        return len(self.stack) - self.consumed

    def ures(self):
        return self.consumed == len(self.stack)


class Problem(ProblemBase):
    def check(self):
        v = Verem()  # üres verem létrehozása
        assert(repr(v) == "[")
        assert(v.ures())
        v.betesz(1)
        v.betesz(4)
        v.betesz(5)
        assert(repr(v) == "[1 4 5")
        assert(v.meret() == 3)
        assert(v.ures() == False)
        x = v.kivesz()
        assert(x == 5)
        assert(repr(v) == "[1 4")
        v.kivesz()
        v.kivesz()  # most már üres
        x = v.kivesz()
        assert(x is None)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

        s = Sor()
        assert(repr(s) == "[")
        assert(s.ures())
        s.hozzaad(1)
        s.hozzaad(2)
        s.hozzaad(3)
        assert(repr(s) == "[1 2 3")
        assert(s.meret() == 3)
        assert(s.ures() == False)
        x = s.kivesz()
        assert(x == 1)
        assert(repr(s) == "[2 3")
        s.kivesz()
        s.kivesz()
        assert(s.meret() == 0)
        assert(s.ures())

if __name__ == "__main__":
    p = Problem()
    p.check()
