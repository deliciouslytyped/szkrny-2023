
# 20121205b Országok, városok
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121205b

import csv
if __name__ == "__main__":
    generator = (line for line in open("countries.csv", "r").readlines() if not line.startswith("#"))
    db = [(orszag, foldresz, fovaros, int(terulet)) for orszag, foldresz, fovaros, terulet in csv.reader(generator, skipinitialspace=True)]
    #(1)
    print(next(iter(sorted(db, key=lambda x: -x[3]))))
    #(2)
    print(sum(1 for _, foldresz, _, _ in db if foldresz == "Africa"))
    #(3)
    print(sum(1 for _, _, _, terulet in db if terulet <= 1000 ))
    #(4)
    print(sum(terulet for _, _, _, terulet in db) / len(db))
    #(5)
    for r in sorted(db, key=lambda x: x[3]):
        print(r)