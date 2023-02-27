
# 20121107a felirat átnevezése
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121107a

from pathlib import Path
import os

here = Path(__file__).parent / "fake"

def genfiles():
    f = ["Dexter.S07E04.HDTV.x264 - ASAP.mp4", "Dexter - 07 x04 - Run.ASAP.English.C.orig.Addic7ed.com.srt"]
    for e in f:
        (here / e).touch()

if __name__ == "__main__":
    genfiles()
    with os.scandir(here) as it:
        for entry in it:
            if any(entry.name.endswith(x) for x in [".avi", ".mkv", ".mp4"]):
                movie = entry
            if entry.name.endswith(".srt"):
                sub = entry
    newname = movie.name.rsplit(".", 1)[0] + ".srt"
    os.rename(sub, here / newname)