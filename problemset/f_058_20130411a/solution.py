
# 20130411a A) random számok ismétlődés nélkül; B) random betűk (duplikátummal)
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130411a

from infra import ProblemBase

import random, itertools, string

class Problem(ProblemBase):
    def run(self):
        print(random.choice(list(itertools.combinations(range(1, 21), 10))))  # TODO there are better ways to do this surely

        r = []
        while not len(set(r)) < len(r):
            r = random.choices(string.ascii_lowercase, k=6)
        print("[" + ", ".join(r) + "] ")

if __name__ == "__main__":
    p = Problem()
    p.check()
