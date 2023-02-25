
# 20121120b Kivételek #2
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121120b

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        def main():
            while True:
                try:
                    szam1 = float(input("1. szam: "))
                    szam2 = float(input("2. szam: "))
                    result = szam1 / szam2
                    print('Az osztas eredmenye: {0:.2f}'.format(result))
                    print('-' * 10)
                except ValueError:
                    print("Olyan értéket adott meg amit nem lehet float-á alakítani.")
                except ZeroDivisionError:
                    print("Hiba: Nullával osztás.")
                except (EOFError, KeyboardInterrupt):
                    break
        main()

if __name__ == "__main__":
    p = Problem()
    p.check()
