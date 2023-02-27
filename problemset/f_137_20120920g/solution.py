
# 20120920g Na de most akkor mi is az én IP címem?
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120920g

from infra import ProblemBase

import requests, json


class Problem(ProblemBase):
    def run(self):
        content = requests.get("https://jsonip.com/").content
        assert(content)
        v = json.loads(content)
        print(v["ip"])

if __name__ == "__main__":
    p = Problem()
    p.check()
