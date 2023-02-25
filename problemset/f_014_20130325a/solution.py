
# 20130325a Osztályok #2 (sor két veremmel) [f7]
# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130325a

from infra import ProblemBase

# https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks

class Sor:
    def __init__(self):
        self.inbox = list()
        self.outbox = list()

    def __repr__(self):
        return "[" + " ".join(repr(x) for x in reversed(self.outbox)) + " ".join(repr(x) for x in self.inbox)

    def append(self, e):
        self.inbox.append(e)

    def popleft(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def size(self):
        return len(self.inbox) + len(self.outbox)

    def is_empty(self):
        return not (self.inbox or self.outbox)

class Problem(ProblemBase):
    def check(self):
        s = Sor()
        assert(repr(s) == "[")
        assert(s.is_empty())
        s.append(1)
        s.append(2)
        s.append(3)
        assert(repr(s) == "[1 2 3")
        assert(s.size() == 3)
        assert(s.is_empty() == False)
        x = s.popleft()
        assert(x == 1)
        assert(repr(s) == "[2 3")
        assert(s.popleft() == 2)
        assert(s.popleft() == 3)
        assert(s.size() == 0)
        assert(s.is_empty())

if __name__ == "__main__":
    p = Problem()
    p.check()
