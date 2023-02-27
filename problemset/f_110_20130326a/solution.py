
# 20130326a utolsó N sor [f10]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130326a

from collections import deque

class Tail:
    def __init__(self, fname, count):
        self.fname = fname
        self.count = count

    def print_lines(self):
        with open(self.fname, "r") as f:
            for l in deque(f.readlines(), maxlen=self.count):
                print(l, end="")

if __name__ == "__main__":
    import sys
    sys.argv.extend(["-5", __file__])
    Tail(sys.argv[2], int(sys.argv[1].lstrip("-"))).print_lines()
