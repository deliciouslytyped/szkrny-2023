# 20221013a Digitális óra a parancssorban
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20221013a

from time import sleep
from datetime import datetime
import sys, os
import curses


digits = [
    [" ┏━┓ ", "  ╻  ", " ┏━┓ ", " ┏━┓ ", " ╻ ╻ ", " ┏━┓ ", " ┏   ", " ┏━┓ ", " ┏━┓ ", " ┏━┓ ", "   "],
    [" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", " ╻ "],
    [" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", "   "],
    [" ┃ ┃ ", "  ┃  ", " ┏━┛ ", " ┣━┫ ", " ┗━┫ ", " ┗━┓ ", " ┣━┓ ", "   ┃ ", " ┣━┫ ", " ┗━┫ ", "   "],
    [" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", "   "],
    [" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ╹ "],
    [" ┗━┛ ", "  ╹  ", " ┗━━ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   "],
]


class Clock:
    def __init__(self, curses=False):
        self.time = None
        self.h = None
        self.m = None
        self.s = None
        self.last_render_size = None
        self.curses = curses

    def on_update(self):
        self.time = datetime.now()
        # note attrs named in concordance with internal fmtspec
        self.h = self.time.hour
        self.m = self.time.minute
        self.s = self.time.second

    def clear(self):  # TODO this doesn't work
        if self.curses:
            self.curses.clear()
        else:
            if self.last_render_size:
                sys.stdout.write("\b"*self.last_render_size)
                os.system("cls")
                #print("cleared %s" % self.last_render_size)

    def render(self, fmtspec="hms"):
        self.clear()
        buffer = list()
        for i in range(len(digits)): # for each font row
            buffer.append("".join([
                (digits[i][getattr(self, spec)//10] + digits[i][getattr(self, spec)%10] +  # numbers
                    (digits[i][-1] if spec != fmtspec[-1] else ""))  # colon if not last specifier
                for spec in fmtspec]))
        if self.curses:
            #https://docs.python.org/3/library/curses.html#curses.window.addstr
            for i, l in enumerate(buffer):
                self.curses.addstr(i, 0, l)
            self.curses.refresh()
        else:
            rendered = "\n".join(buffer)
            self.last_render_size = len(rendered)
            print(rendered)

    def loop(self, fmtspec="hms"):
        while True:
            sleep(0.2)  # TODO
            self.on_update()
            self.render(fmtspec=fmtspec)

def curses_wrapper(f):
    def ff(a):
        return f(curses=a)
    return curses.wrapper(ff)


if __name__ == "__main__":
    sys.argv.append("-hms")
    fmtspec = sys.argv[1].lstrip("-")

    c = curses_wrapper(Clock)
    c.loop(fmtspec=fmtspec)