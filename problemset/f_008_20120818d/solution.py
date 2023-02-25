
# 20120818d List comprehensions [f4]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818d

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.f1(['auto', 'villamos', 'metro']) == ['AUTO!', 'VILLAMOS!', 'METRO!'])
        assert(self.f2(['aladar', 'bela', 'cecil']) == ['Aladar', 'Bela', 'Cecil'])
        assert(self.f3() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert(self.f4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        assert(self.f5(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert(self.f6("1234567") == [1, 2, 3, 4, 5, 6, 7])
        assert(self.f7('The quick brown fox jumps over the lazy dog') == [3, 5, 5, 3, 5, 4, 3, 4, 3])
        assert(self.f8("python is an awesome language") == ['p', 'i', 'a', 'a', 'l'])
        assert(self.f9('The quick brown fox jumps over the lazy dog') == [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)])
        assert(self.f10() == [0, 2, 4, 6, 8])
        assert(self.f11() == [0, 4, 16, 36, 64, 100, 144, 196, 256, 324])
        assert(self.f12() == [4, 64, 144, 324])
        assert(self.f13() == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        assert(self.f14([' apple ', ' banana ', ' kiwi']) == ['apple', 'banana', 'kiwi'])
        assert(self.f15([1, 0, 1, 1, 0, 1, 0, 0]) == "10110100")

    def f1(self, l):
        return [x.upper()+"!" for x in l]

    def f2(self, l):
        return [x.capitalize() for x in l]

    def f3(self):
        return [0]*10

    def f4(self, l):
        return [x*2 for x in l]

    def f5(self, l):
        return [int(x) for x in l]

    def f6(self, s):
        return [int(x) for x in s]

    def f7(self, s):
        return [len(w) for w in s.split()]

    def f8(self, s):
        return [w[0] for w in s.split()]

    def f9(self, s):
        return [(w, len(w)) for w in s.split()]

    def f10(self):
        return [x*2 for x in range(5)]

    def f11(self):
        return [x**2 for x in range(20) if not x**2 % 2]

    def f12(self):
        return [x**2 for x in range(20) if x**2 % 10 == 4]

    def f13(self):
        return "".join([chr(x) for x in range(ord('A'), ord('Z')+1)])

    def f14(self, l):
        return [x.strip() for x in l]

    def f15(self, l):
        return "".join(str(x) for x in l)

if __name__ == "__main__":
    p = Problem()
    p.check()
