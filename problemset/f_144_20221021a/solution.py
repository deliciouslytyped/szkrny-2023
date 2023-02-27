# TODO ez az egész kicsit tákolt mert kétfel figyeltem


# 20221021a Végső visszaszámlálás
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20221021a

import os, sys
from pathlib import Path
import winsound
import argparse
import re
import curses
from time import sleep
from datetime import datetime, timedelta

here = Path(__file__).parent

class Timer:
    def __init__(self, argv, curses=None):
        self.h = 0
        self.m = 0
        self.s = 0 # TODO inited these to 0 because something is screwy with the argparse, set to None to debug
        self.n = None
        self.curses = curses
        self.targetTime = None
        self.parseArgs(argv)
        self.calcTarget()

    def ring(self, n):
        # TODO branch on platform
        for i in range(n):
            winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

    def parsetime(self, s):
        assert(s) #TODO this doesnt trigger when the arg isnt passed??
        r = re.findall("([0-9]+(h|m|s))", s)
        for e in ["h", "m", "s"]:
            assert(len([1 for x in r if x[0] == e]) <= 1) #TODO error handling
        for e, _ in r:
            setattr(self, e[-1], int(e[:-1])) #TODO this has sideeffects, not how this should be done

    def parseArgs(self, argv):
        parser = argparse.ArgumentParser()
        parser.add_argument("time", nargs="?", type=self.parsetime)
        parser.add_argument("-p", type=int, default=3)
        args = parser.parse_args()  #TODO unclusterf this
        self.n = args.p

    def calcTarget(self):
        self.targetTime = datetime.now() + timedelta(hours=self.h, minutes=self.m, seconds=self.s)

    def render(self):
        self.clear()
        if self.targetTime > datetime.now():  # TODO if reversed somehow -1 day
            delta = (self.targetTime - datetime.now()).seconds
            h = delta // 3600
            m = (delta % 3600) // 60
            s = (delta % 60)
        else:
            h, m, s = 0, 0, 0
        buf = f"{h:02}:{m:02}:{s:02}"
        if self.curses:
            self.curses.addstr(0, 0, buf)
            self.curses.refresh()
        else:
            print(buf)

    def clear(self):  # TODO this doesn't work
        if self.curses:
            self.curses.clear()
        else:
            #sys.stdout.write("\b"*self.last_render_size)
            # since its a single line, in this case \r would also work
            os.system("cls")

    def loop(self):
        while True:
            sleep(0.2)  # TODO
            self.render()
            if datetime.now() >= self.targetTime:
                self.ring(self.n)
                break

def curses_wrapper(f, *args):
    def ff(a):
        return f(*args, curses=a)
    return curses.wrapper(ff)

if __name__ == "__main__":
    sys.argv.append("-p2")
    c = curses_wrapper(Timer, sys.argv)
    c.loop()
