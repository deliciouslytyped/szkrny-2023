
# 20150402a Reguláris kifejezések
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20150402a

from infra import ProblemBase

from textwrap import dedent

text = dedent("""
    2015. április
    =============
    
    díjak: http://www.agavekonyvek.hu/szallitasi-dijaink
    Az árak Ft-ban értendők.
    
    * http://www.agavekonyvek.hu/agave/science-fiction/az-idoutazas-tegnapja.html (J)
      2 067 Ft
      Várható megjelenés: 2015.05.05.
    
    * http://www.agavekonyvek.hu/agave/thriller/az-utolso-varos.html (L)
      2 235 Ft
    
    * http://www.agavekonyvek.hu/agave/science-fiction/voros-lazadas-arany-haboru.html (L)
      4 872 Ft""").strip()

import re

class Problem(ProblemBase):
    def check(self):
        assert(self.run(text) == dedent("""
            2,067 Ft
            2,235 Ft
            4,872 Ft
            
            Szumma: 9,174 Ft
            """).lstrip())

    def run(self, s):
        acc = ""

        r = re.findall("([0-9 ]+) Ft", s)
        r = [int("".join(x.split())) for x in r]
        for e in r:
            acc += f"{e:,} Ft\n"
        acc += "\n"

        x = sum(r)
        acc += f"Szumma: {x:,} Ft\n"

        print(acc)
        return acc

if __name__ == "__main__":
    p = Problem()
    p.check()
