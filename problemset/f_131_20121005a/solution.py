
# 20121005a Keresés a PI számjegyeiben
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121005a

from infra import ProblemBase

from math import sqrt, factorial, floor
from decimal import *

def isprime(n):
    for i in range(2, floor(sqrt(n)+1)):
        if not n % i:
            return False
    return True

def calc_pi():
    k_1 = 545140134
    k_2 = 13591409
    k_3 = 640320
    k_4 = 100100025
    k_5 = 327843840
    k_6 = 53360

    s = 0
    i = 0
    getcontext().prec = 10000
    while i < getcontext().prec / 14:
        s += (-1) ** i * Decimal(factorial(6 * i) * (k_2 + i * k_1)) / Decimal(
            factorial(i) ** 3 * factorial(3 * i) * (8 * k_4 * k_5) ** i)
        i += 1
        pi = k_6 * Decimal.sqrt(Decimal(k_3)) / s

    print(pi)
    return pi

class Problem(ProblemBase):
    has_check = True
    def run(self):
        #pi = calc_pi()
        ss = open("pi1m.txt", "r").read().strip()[2:]
        #ss = str(pi)[2:]
        kk = 7
        for i in range(len(ss)):
            if len(str(int(ss[i:i+kk]))) == kk and tuple(ss[i:i+kk]) == tuple(reversed(ss[i:i+kk])) and isprime(int(ss[i:i+kk])):
                res = ss[i:i+kk]
                print(ss[i:i+kk])
                break

        return res

if __name__ == "__main__":
    p = Problem()
    p.check()
