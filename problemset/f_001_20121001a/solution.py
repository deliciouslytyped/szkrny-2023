
# 20121001a Sztring metódus [f1]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121001a

from infra import ProblemBase

class Problem(ProblemBase):
    def check(self):
        assert(self.masikfeladat() == "Hello Laci!")

    def egyikfeladat(self):
        # Olvassuk ki a kommentekkel kezdődő sorokat a fajlból.
        with open(__file__, "rb") as f:
            lines = f.read().decode("utf8").splitlines()
            print("\n".join(l for l in lines if l.lstrip().startswith("#")))

    def masikfeladat(self):
        def input(prompt): # fake input fgv
            return "         Laci           "

        s = input("Name:")
        return "Hello %s!" % s.strip()

if __name__ == "__main__":
    p = Problem()
    p.check()
