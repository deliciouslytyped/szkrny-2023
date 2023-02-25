
# 20130218c karakterszámláló [f6]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130218c

from infra import ProblemBase

from collections import Counter
import string


def fill(d):
    for i in string.ascii_lowercase:
        if i not in d:
            d[i] = 0
    return d


class Problem(ProblemBase):
    def check(self):
        assert(self.run("cat and dog") == fill({'whitespace': 2, 'others': 0, 'a': 2, 'c': 1, 'd': 2, 'g': 1, 'n': 1, 'o': 1, 't': 1}))

    def run(self, s):
        def fix(d):
            d['whitespace'] = d[' ']
            del d[' ']
            old = sum(d.values())
            d = {k:v for k, v in d.items() if k in string.ascii_lowercase or k == "whitespace"}
            d['others'] = old - sum(d.values())
            return d
        r = fix(fill(Counter(s)))
        print(r)
        return r

if __name__ == "__main__":
    p = Problem()
    p.check()
