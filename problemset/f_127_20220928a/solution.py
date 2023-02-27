
# 20220928a mappa tartalmának kilistázása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20220928a

from pathlib import Path
import os

here = Path(__file__).parent.parent

def listdir(path):
    dirs = list()
    files = list()
    for e in os.scandir(path):
        if e.is_dir():
            dirs.append(e)
        if e.is_file():
            dirs.append(e)
    for e in sorted(dirs, key=lambda x: x.name):
        print(e.name)
    for e in sorted(files, key=lambda x: x.name):
        print(e.name)

if __name__ == "__main__":
    listdir(here)
    print()
    listdir(here / "f_126_20151111a")
