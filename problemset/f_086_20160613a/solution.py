
# 20160613a Hatoslottó
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20160613a

from infra import ProblemBase

from itertools import product, combinations
from math import prod
from collections import defaultdict

class Problem(ProblemBase):
    def run(self):
        factors = defaultdict(int)
        target = 996300
        i = 2
        while target > 1:
            if target % i == 0:
                target /= i
                factors[i] += 1
                i = 2
            else:
                i += 1

        factors, powers = zip(*factors.items())
        num = lambda powers: prod(map(lambda t: pow(*t), zip(factors, powers)))
        clamp = lambda l: [x for x in l if 1 <= x <= 45]
        power_counter = product(*[range(p+1) for p in powers])
        possible_numbers = clamp([num(ps) for ps in power_counter])
        r = [x for x in combinations(possible_numbers, 6) if sum(x) == 90 and prod(x) == 996300]
        print(r)

if __name__ == "__main__":
    p = Problem()
    p.check()
