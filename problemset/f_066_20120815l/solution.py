
# 20120815l Rejtélyes üzenet [f3]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815l

from infra import ProblemBase

from textwrap import dedent
import string

class Problem(ProblemBase):
    c = dedent("""
        Cbcq Dgyk!
        
        Dmeybh kce cew yrwyg hmrylyaqmr:
        rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
        
        Aqmimjjyi:
        
        Ynyb
        """)

    def run(self):
        rotate = 2
        print(self.c.translate(str.maketrans(string.ascii_letters, string.ascii_letters[rotate:] + string.ascii_letters[:rotate])))

if __name__ == "__main__":
    p = Problem()
    p.check()
