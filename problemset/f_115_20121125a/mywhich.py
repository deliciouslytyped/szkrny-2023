
# 20121125a my which
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121125a

import os, sys
from pathlib import Path

if __name__ == "__main__":
    sys.argv.append("cmd.exe")
    query = sys.argv[1]

    search = os.environ["PATH"].split(";")  # TODO platform specific
    for p in search:
        try:
            with os.scandir(p) as it:
                for entry in it:
                    if entry.is_file() and entry.name == query:
                        print(Path(entry.path) / entry.name)
                        sys.exit(0)
        except FileNotFoundError:
            pass
    sys.exit(-1)
