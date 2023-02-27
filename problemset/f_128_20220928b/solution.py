
# 20220928b my touch
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20220928b

import os, sys

if __name__ == "__main__":
    sys.argv.append("test.txt")

    if len(sys.argv) != 2:
        print("Nem megfelelő számú argumentum!")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "w") as f:
            pass