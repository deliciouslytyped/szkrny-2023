
# 20130321a mp3-ak összeválogatása
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130321a

import shutil
import os
from pathlib import Path
from random import choice

BYTE = 1
KB = 1024 * BYTE
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB

class Picker:
    def __init__(self, source, max):
        self.sourcedir = source
        self.max = max

    def genlist(self):
        files = set()
        with os.scandir(self.sourcedir) as it:
            for entry in it:
                if entry.name.endswith(".mp3") and entry.is_file():
                    files.add((entry, entry.stat().st_size + int(entry.name.split("size_")[1].replace(".mp3","")))) # incorporate fake size

        collection = list()
        acc = 0
        while files:
            file = choice(list(files))  # TODO doing this conversion constantly is inefficient but set() doesn't support choice()
            files.remove(file)
            if acc + file[1] < self.max:
                acc += file[1]
                collection.append(file[0])
        print("%sGB collected" % (acc/(1*GB)))
        return collection

    def copy(self, target):
        assert(target.is_dir())
        files = self.genlist()
        print(files)
        for f in files:
            shutil.copy(f, target)

if __name__ == "__main__":
    Picker( Path(__file__).parent / "fakesource", 1*GB).copy(Path(__file__).parent / "fakedest")