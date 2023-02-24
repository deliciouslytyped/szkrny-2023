
# 20141019a kedvenc subreddit-ek megnyitása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20141019a

from infra import ProblemBase

import webbrowser

class Problem(ProblemBase):
    def run(self):
        reddits = ["netsec", "sysadmin", "remath"]
        url = "https://old.reddit.com/r/%s"
        webbrowser.open_new(url % reddits[0])
        for r in reddits[1:]:
            webbrowser.open(url % r)

if __name__ == "__main__":
    p = Problem()
    p.check()
