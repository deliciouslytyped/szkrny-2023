
# 20120816b get_alap.py
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120816b

from textwrap import dedent
from pathlib import Path
import shutil
import sys

try:
    here = Path(__file__).parent
except NameError:
    here = Path(sys.argv[0]).parent

class Templater:
    def __init__(self):
        self.list = [("Python", "py"), ("C", "c")]

    def render(self):
        print(dedent(f"""
            ---------------------------
            Create an empty source file
            ---------------------------""").strip())

        maxln = max([len(x) for x,_ in self.list])
        for i, (name, extension) in enumerate(self.list):
            print(f"{i+1}) {name:<{maxln}} [{extension}]")

        print(dedent("""
            q) quit
            """).strip())

    def run(self, target=None):
        if not target:
            self.interactive_run()
        else:
            self.copy(target)

    def interactive_run(self):
        self.render()
        r = int(input("> "))
        ext = self.list[r-1][1]
        self.copy(ext)

    def copy(self, ext):
        if (here / f"main.{ext}").exists():
            print(f"Hiba: a main.{ext} fajl már létezik!")
        else:
            shutil.copy(here / "templates" / f"template.{ext}", here / f"main.{ext}")


if __name__ == "__main__":
    sys.argv.append("py")

    t = Templater()
    if len(sys.argv) > 1:
        t.run(sys.argv[1])
    else:
        t.run()