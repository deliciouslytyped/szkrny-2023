#WIP ...ez lehetetlen 256byteba??

hmn = """Isten, áldd meg a magyart
Jó kedvvel, bőséggel,
Nyújts feléje védő kart,
Ha küzd ellenséggel;
Bal sors akit régen tép,
Hozz rá víg esztendőt,
Megbűnhődte már e nép
A múltat s jövendőt!

Őseinket felhozád
Kárpát szent bércére,
Általad nyert szép hazát
Bendegúznak vére.
S merre zúgnak habjai
Tiszának, Dunának,
Árpád hős magzatjai
Felvirágozának."""

from itertools import tee
import zlib
import lzma

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


##hmn = "\n".join([l[0].lower()+l[1:] if l else "" for l in hmn.split("\n")])
#ff = zlib.compressobj(9, wbits=-15)
#ff.compress(hmn.encode("iso8859-2"))
#print(len(ff.flush()))

#my_filters = [
#    {"id": lzma.FILTER_LZMA1, "preset": 9 | lzma.PRESET_EXTREME},
#]
#print(len(lzma.compress(hmn.encode("iso8859-2"), format=lzma.FORMAT_RAW, filters=my_filters)))

#ff = zlib.compressobj(9, wbits=-15)
#fff = hmn.translate(str.maketrans("áéüúöűőŐÁóí","OqVCEXQwWPU"))
#fff = "\n".join([l[0].lower()+l[1:] if l else "" for l in fff.split("\n")])
#print(fff)
#ff.compress(fff.encode("iso8859-2"))
#print(len(ff.flush()))

import string
from itertools import permutations, combinations
from random import shuffle
free = set(string.ascii_letters) - set(hmn)
cleaned = "\n".join([x[0].lower()+x[1:] if x else x for x in hmn.splitlines()])
free2 = set(string.ascii_letters) - set(cleaned)
print(cleaned)
print(free)
print(free2)
m = 500
for p in combinations(free, 15):
    p = list(p)
    shuffle(p)
    for pp in permutations(p):
        ff = zlib.compressobj(9, wbits=-9)
        fff = cleaned.translate(str.maketrans("áéüúöűőóí.! ,\n;", "".join(pp)))
        ff.compress(fff.encode("ascii"))
        res = ff.flush()
        if (v := min(m, len(res))) < m:
            m = v
            print(f"{m} {''.join(p)}")
            print(repr(res))

#from zlib import decompress as d;d("", wbits=-9)