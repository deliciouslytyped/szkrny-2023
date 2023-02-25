
# 20121006e Haladó rendezés
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121006e

from infra import ProblemBase

class Problem(ProblemBase):
    def run(self):
        print(self.problem1())
        print(self.problem2())
        print(self.problem3())

    def problem1(self):
        data = [
            (1, 'Albany', 'NY', 162692),
            (3, 'Allegany', 'NY', 11986),
            (121, 'Wyoming', 'NY', 8722),
            (123, 'Yates', 'NY', 5094)
        ]
        return list(sorted(data, key=lambda x: x[3]))

    def problem2(self):
        users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
        return list(sorted(users, key=lambda x: x.split(":")[1], reverse=True))

    def problem3(self):
        li = [[2, 6], [1, 3], [5, 4]]
        return list(sorted(li, key=lambda x: x[1]))

if __name__ == "__main__":
    p = Problem()
    p.check()
