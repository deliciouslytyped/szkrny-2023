
# 20130218d sztring inkrementálása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130218d

from infra import ProblemBase

import string


class Problem(ProblemBase):
    def check(self):
        assert(self.run("a") == "b")
        assert(self.run("z") == "aa")
        assert(self.run("aa") == "ab")
        assert(self.run("am") == "an")
        assert(self.run("ba") == "bb")
        assert(self.run("bz") == "ca")
        assert(self.run("zza") == "zzb")
        assert(self.run("zzz") == "aaaa")
        assert(self.run("aaaz") == "aaba")

    def run(self, s):
        ss = list(reversed(s))
        i = 0
        carry = 0
        while carry or i == 0:
            if i < len(s):
                idx = string.ascii_lowercase.find(ss[i]) + (1 if i == 0 else 0) + carry
                ss[i] = string.ascii_lowercase[idx % 26]
                carry = idx // 26
            else:
                ss.append("a")
                carry = 0
            i += 1
        return "".join(reversed(ss))

if __name__ == "__main__":
    p = Problem()
    p.check()
