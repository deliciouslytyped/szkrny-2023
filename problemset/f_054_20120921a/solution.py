
# 20120921a Ékezetek eltávolítása [f5]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120921a

from infra import ProblemBase

from textwrap import dedent

class Problem(ProblemBase):
    def check(self):
        assert(self.run().startswith("A katalan zaszlo, a Senyera szineit fogja viselni a kovetkezo ideny"))
        assert(self.run() == self.alternative())

    def alternative(self):
        text = dedent("""
            A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

            A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

            A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
            """).strip()

        d = dict(zip("áéíóöőúüűÁÉÍÓÖŐÚÜŰ", "aeiooouuuAEIOOOUUU"))
        return "".join([d[x] if x in d else x for x in text])

    def run(self):
        text = dedent("""
            A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.
            
            A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.
            
            A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
            """).strip()
        return text.translate(str.maketrans("áéíóöőúüűÁÉÍÓÖŐÚÜŰ", "aeiooouuuAEIOOOUUU"))

if __name__ == "__main__":
    p = Problem()
    p.check()
