
# 20120815k Szökés Alcatrazból
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815k

from infra import ProblemBase

# TODO na oke igen de mi is történik itt? / Fast solution?
class Problem(ProblemBase):
    has_check = True
    def run(self):
        size = 600
        doors = [False]*size
        for i in range(0, size):
            j = i
            while j < size:
                doors[j] = not doors[j]
                j += (i+1)
            print("".join([("1" if d else "0") for d in doors]))
        result = [i+1 for i, x in enumerate(doors) if x]
        print(result)
        return "".join([str(x) for x in result])

if __name__ == "__main__":
    p = Problem()
    p.check()
