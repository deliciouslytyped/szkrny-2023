
# 20130424a programozási nyelvek
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130424a

from infra import ProblemBase

from lxml.html.soupparser import parse
from lxml.etree import tostring
from io import BytesIO
import requests

class Problem(ProblemBase):
    def run(self):
        content = requests.get("https://en.wikipedia.org/w/index.php?title=List_of_programming_languages&action=edit").content
        assert(content)
        etree = parse(BytesIO(content))
        strdata = etree.xpath('//*[@id="wpTextbox1"]')[0].text
        ll = [x for x in strdata.splitlines() if x.startswith("* [[")]
        lastidx = ll.index("* [[Z++]]")
        print(lastidx+1)

if __name__ == "__main__":
    p = Problem()
    p.check()
