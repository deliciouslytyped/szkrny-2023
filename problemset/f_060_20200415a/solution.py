
# 20200415a Naprendszer
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20200415a

from infra import ProblemBase

import requests
import csv
import re
from io import StringIO

class Problem(ProblemBase):
    def run(self):
        _csv = requests.get("https://raw.githubusercontent.com/jabbalaci/Programozas_1/main/datasets/DT2.csv").content
        assert(_csv)
        words = [ r[0] for r in csv.reader(StringIO(_csv.decode("utf8"))) if re.match(".*J.*S.*U.*N.*", r[0], re.IGNORECASE) ]
        print(words)

if __name__ == "__main__":
    p = Problem()
    p.check()
