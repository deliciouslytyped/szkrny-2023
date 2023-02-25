
# 20121120a Kivételek #1
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121120a

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        import sys

        def cat(fname):
            f = open(fname, 'r')
            text = f.read()
            print('---', fname)
            print(text)
            f.close()

        sys.argv.extend(["test1.txt", "test2.txt"])
        args = sys.argv[1:]
        for arg in args:
            try:
                cat(arg)
            except FileNotFoundError:
                continue

if __name__ == "__main__":
    p = Problem()
    p.check()
