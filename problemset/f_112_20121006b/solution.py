
# 20121006b mass download
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121006b

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        #mj.: ez a feladat konnyen megoldhato csupan a curl parancs range featurejével.
        url = "http://example.com/galleryFX/%s.jpg"
        # a feladat
        for i in range(15):
            print(url % i)
        print()
        # b feladat
        for i in range(15):
            print(url % f"{i:02}")

if __name__ == "__main__":
    p = Problem()
    p.check()
