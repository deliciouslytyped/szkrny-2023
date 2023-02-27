
# 20131002a file keresése egy könyvtárban rekurzívan
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20131002a

from pathlib import Path
from hashlib import md5
import os, sys

here = Path(__file__).parent

def hashfile(file):
    m = md5()
    with open(file, "rb") as f:
        while b := f.read(8192):
            m.update(b)
    return m.hexdigest()

if __name__ == "__main__":
    sys.argv.append("test.txt")
    target = hashfile(sys.argv[1])
    print("Target: " + target)

    for dirpath, _, filenames in os.walk(here):
        dir = Path(dirpath)
        for filen in filenames:
            file = dir / filen
            if hashfile(file) == target:
                print(file)
                sys.exit(0)
    sys.exit(1)