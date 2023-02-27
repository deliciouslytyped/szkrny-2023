
# 20120920a JPG file-ok átnevezése
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120920a

from pathlib import Path
import os

here = Path(__file__).parent

def genfiles():
    for i in range(656, 683+1):
        (here / "fake" / f"DSFC{i}.JPG").touch()

if __name__ == "__main__":
    genfiles()
    files = list()
    with os.scandir(here / "fake") as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith("JPG"):
                files.append(entry)
    for i,e in enumerate(sorted(files, key=lambda e: e.name)):
        print(f"Renaming {e.name} to {i:04}.jpg")
        os.rename(e, here / "fake" / f"{i:04}.jpg")