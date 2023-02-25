
# 20210805a bing.com háttérkép
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20210805a

from infra import ProblemBase

import requests
from lxml.html.soupparser import parse
from io import BytesIO

class Problem(ProblemBase):
    def run(self):
        content = requests.get("https://www.bing.com").content
        assert(content)
        etree = parse(BytesIO(content))
        url = [x for x in etree.xpath('//meta[@property="og:image"]')][0].attrib["content"]
        print(url)
        return url

if __name__ == "__main__":
    p = Problem()
    p.check()
