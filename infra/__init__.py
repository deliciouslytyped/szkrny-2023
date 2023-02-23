import requests
import inspect
import pathlib
from lxml.html.soupparser import parse
from lxml.etree import tostring
from io import BytesIO


def clean_tree(etree):
    elem = etree.xpath('/html/body/form')[0]
    elem.getparent().remove(elem)
    head = etree.xpath('/html/head')[0]
    head.getparent().remove(head)


class ProblemBase:
    check_url = "https://arato.inf.unideb.hu/szathmary.laszlo/python-solution-checker/check.php?id="
    has_check = False

    def check(self):
        verdict, html, etree = self._check()
        #if verdict:
        #    print("Solution is good!")
        #else:
        #    print("Solution is bad!")
        #print(html)
        print(etree.xpath('//p')[1].text_content())  # TODO
        return verdict

    def _check(self):
        if self.has_check:
            problemid = self.getID()
            result = self.run()
            resp = requests.post(f"{self.check_url}{problemid}", data={"solution":f"{result}"})
            assert(resp.status_code == 200)
            etree = parse(BytesIO(resp.content))
            clean_tree(etree)
            html = tostring(etree, encoding="unicode")
            if html.find("good.png") != -1:  # TODO meh
                verdict = True
            elif html.find("bad.png") != -1:
                verdict = False
            else:
                raise AssertionError
            return (verdict, html, etree)

    def getID(self):
        s = inspect.stack()
        f = pathlib.Path(s[3].filename)  # WARNING this is fragile / TODO
        assert(f.name == "solution.py")  # TODO maybe this doesn't need to be this strict
        return f.parent.name.split("_")[2]