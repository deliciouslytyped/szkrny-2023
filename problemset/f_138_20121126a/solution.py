
# 20121126a /r/EarthPorn
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121126a

from infra import ProblemBase

import requests, json
f

class Problem(ProblemBase):
    def run(self):
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'})
        content = session.get("https://www.reddit.com/r/earthporn/.json").content
        assert(content)
        d = [x["data"]["url_overridden_by_dest"] for x in json.loads(content)["data"]["children"] if "url_overridden_by_dest" in x["data"]]
        for e in d:
            #with open(e.rsplit("/")[-1], "wb") as f:
            #    f.write(requests.get(e).content)
            print(e) # Nem fogom szpemmelni a szervert, nem toltjuk le az osszes massziv képet

if __name__ == "__main__":
    p = Problem()
    p.check()
