
# 20170702a Számkitalálós
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20170702a

from infra import ProblemBase

from random import randint

class Problem(ProblemBase):
    def run(self):
        print("Number Guessing Game")
        print("--------------------")
        r = randint(1, 100)
        n = 0
        print("I thought of a number between 1 and 100.")
        while (v := int(input("your guess> ")), n := n + 1) != r:
            if v == r:
                print("Good job! That's it!")
                print(f"Number of guesses: {n}")
                break
            print("my number is %s" % ("larger" if v < r else "smaller"))

if __name__ == "__main__":
    p = Problem()
    p.check()
