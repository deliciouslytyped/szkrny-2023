import requests
import requests_cache
from lxml.html.soupparser import parse
#from lxml.etree import tostring
from io import BytesIO
import pathlib
from textwrap import dedent
import logging

requests_cache.install_cache('demo_cache')  # https://pypi.org/project/requests-cache/
thisfile = pathlib.Path(__file__)
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().addHandler(logging.FileHandler(thisfile.parent / "problemgen.log"))
logging.getLogger().setLevel(logging.DEBUG)


def gen_solution_template(name, shortdesc, url):
    template = dedent(f"""
        # {name} {shortdesc}
        # {url}

        from infra import ProblemBase

        class Problem(ProblemBase):
            pass
            
        if __name__ == "__main__":
            p = Problem()
            p.check()
        """)
    return template


class ProjectGenerator:
    url = "https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py.Feladatok2023febr"

    def __init__(self):
        self.response = None
        self.problemElems = None
        self.problems = None
        self.problemsetPath = thisfile.parent.parent / "problemset"

    def get_problems(self):
        res = requests.get(self.url)
        assert(res.status_code == 200)
        self.response = res
        etree = parse(BytesIO(res.content))  # TODO seriously?
        #content = tostring(etree, encoding="utf-8")  # Make sure we are using UTF8 # TODO: does this do what I think it does?
        #etree = parse(BytesIO(content))
        self.problemElems = etree.xpath('//li/a[contains(@href, "Py3.")]/..')
        # [['20221021a',
        #   'Végső visszaszámlálás',
        #   'https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20221021a'], ...]
        self.problems = [x.text_content().strip().split(" ", 1) + [x.find("a").attrib["href"]] for x in self.problemElems]

    def gen_problemset(self):
        self.problemsetPath.mkdir(exist_ok=True)
        for i, (name, desc, url) in enumerate(self.problems):
            problemDir = self.problemsetPath / f"f_{i:03}_{name}"
            problemDir.mkdir(exist_ok=True)
            problemFile = problemDir / "solution.py"
            with open(problemFile, "wb") as f:
                logging.info(f"Writing {problemFile} .")
                f.write(gen_solution_template(name, desc, url).encode("utf8"))


if __name__ == "__main__":
    pj = ProjectGenerator()
    pj.get_problems()
    pj.gen_problemset()
