#!/usr/bin/env python3

import numpy as np


class MyList:
    INITIAL_CAPACITY = 4
    MULTIPLIER = 2

    def __init__(self):
        self._array = np.empty(MyList.INITIAL_CAPACITY, dtype='object')
        self._capacity = MyList.INITIAL_CAPACITY
        self._size = 0

    def append(self, value):
        if self._capacity <= self._size:
            oldarray = self._array
            self._capacity *= 2
            self._array = np.empty(self._capacity, dtype='object')
            np.copyto(self._array[0:len(oldarray)], oldarray)

        self._array[self._size] = value
        self._size += 1


    def pop(self):
        assert(self._size)
        r = self._array[self._size-1]
        self._size -= 1
        return r

    def __repr__(self):
        return "[" + ", ".join(repr(x) for i, x in enumerate(self._array) if i < self._size) + "]"

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._array[:self._size])


def main():
    s = MyList()
    assert (repr(s) == "[]")
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(2)
    s.append(3)
    assert (repr(s) == "[1, 2, 3, 2, 3]")
    assert (len(s) == 5)
    x = s.pop()
    assert (x == 3)
    assert (repr(s) == "[1, 2, 3, 2]")
    assert (s.pop() == 2)
    assert (s.pop() == 3)
    assert (len(s) == 2)


##############################################################################

if __name__ == "__main__":
    main()