
# 20120910a Hangrend [f4]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120910a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.run("ablak") == "mély")
        assert(self.run("erkély") == "magas")
        assert(self.run("kisvasút") == "vegyes")
        assert(self.run("magas") == "mély")
        assert(self.run("mély") == "magas")
        assert(self.run("Pfffffff") == "semmilyen")

    def run(self, s):
        mely = set("aáoóuú")
        magas = set("eéiíöőüű")

        mely = bool(mely & set(s))
        magas = bool(magas & set(s))
        if not (mely or magas):
            return "semmilyen"
        elif mely and magas:
            return "vegyes"
        elif mely:
            return "mély"
        else:
            return "magas"


if __name__ == "__main__":
    p = Problem()
    p.check()
