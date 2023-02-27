
# 20121205c subprocess modul
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121205c

import subprocess
import cmd

class Query(cmd.Cmd):
    intro = """1. Windows verzió lekérdezése\n2.???"""

    def do_1(self, arg):
        subprocess.run("ver", shell=True)

    def do_2(self, arg):
        pass

    def do_q(self, arg):
        return True

if __name__ == "__main__":
    Query().cmdloop()