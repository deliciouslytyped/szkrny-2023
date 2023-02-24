
# 20140215b egyszerű progress indicator
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20140215b

from infra import ProblemBase

import time

class Problem(ProblemBase):
    def run(self):
        print("Downloading images...", end="")
        l = ["|", "/", "-", "\\"]
        for i in range(0, 20):
            time.sleep(0.3)
            print("\x08" + l[i % len(l)], end="")

if __name__ == "__main__":
    p = Problem()
    p.check()
