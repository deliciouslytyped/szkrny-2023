
# 20130905a Programozói kifogások
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130905a

from infra import ProblemBase

import requests
from lxml.html.soupparser import parse
from io import BytesIO

class Problem(ProblemBase):
    def run(self):
        content = requests.get("http://developerexcuses.com/").content
        assert(content)
        etree = parse(BytesIO(content))
        print(etree.xpath("//a[@href='/']")[0].text)

if __name__ == "__main__":
    p = Problem()
    p.check()
