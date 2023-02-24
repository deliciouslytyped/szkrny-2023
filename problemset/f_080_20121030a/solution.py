
# 20121030a Bullshit Generátor [f8]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121030a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        # Stupid import bullshit https://stackoverflow.com/questions/16981921/relative-imports-in-python-3#comment33977735_16985066
        import os, sys, inspect
        SCRIPT_DIR = os.path.dirname(inspect.getfile(inspect.currentframe()))
        sys.path.append(os.path.dirname(SCRIPT_DIR))
        from bullshit import get_bullshit
        r = get_bullshit()
        print(r)
        assert(r)

if __name__ == "__main__":
    p = Problem()
    p.check()
