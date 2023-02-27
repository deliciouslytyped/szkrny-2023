
# 20151111a Azonos tartalmú file-ok keresése
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20151111a

from pathlib import Path
from hashlib import md5
import os
from collections import defaultdict

here = Path(__file__).parent / "fake"

def hashfile(file):
    m = md5()
    with open(file, "rb") as f:
        while b := f.read(8192):
            m.update(b)
    return m.hexdigest()

if __name__ == "__main__":
    hashes = defaultdict(list)

    for dirpath, _, filenames in os.walk(here):
        dir = Path(dirpath)
        for filen in filenames:
            file = dir / filen
            hashes[hashfile(file)].append(file)

    for k, v in hashes.items():
        if len(v) > 1:
            print(f"Duplicates of {v[0]} ({k})")
            for e in v[1:]:
               print("\t%s" % e)