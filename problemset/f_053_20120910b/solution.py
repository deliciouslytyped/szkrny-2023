
# 20120910b Magánhangzók eltávolítása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120910b

from infra import ProblemBase

from textwrap import dedent

class Problem(ProblemBase):
    def run(self):
        text = dedent("""
            A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

            A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

            A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
            """).strip()
        print(text.translate(str.maketrans("", "", "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ")))

if __name__ == "__main__":
    p = Problem()
    p.check()
