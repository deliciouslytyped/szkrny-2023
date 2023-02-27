
# 20121126b Két program közti kommunikáció
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121126b

from infra import ProblemBase

import json
from math import sqrt, floor

def primegen():
    l = [True] * (10_000_000-2)
    for i in range(2, floor(sqrt(len(l)))+1):
        if l[i-2]:
            for k in range(i-2+i, len(l), i):
                l[k] = False

    json.dump([i+2 for i, v in enumerate(l) if v], open("primes.json", "w"))

def palindromeprimes():
    d = json.load(open("primes.json", "r"))
    for e in d:
        if tuple(str(e)) == tuple(reversed(str(e))):
            print(e)

if __name__ == "__main__":
    primegen()
    palindromeprimes()