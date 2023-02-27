
# 20191012b Münchausen számok
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20191012b

from infra import ProblemBase


import pprint
from multiprocessing import Pool
import pyximport
pyximport.install(pyimport=True)
from munch import munchies, digits, _pows # with cython, though this super messy right now

class Problem(ProblemBase):
    def run(self):
        pass

if __name__ == "__main__":
    with Pool(processes=8) as pool:
        print(list(x for x in sum(pool.map(munchies, [(i*10_000_000, (i+1) * 10_000_000) for i in range(0, 44)]), []) if x))
