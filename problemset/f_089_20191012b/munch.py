import cython


def digits(x: cython.int):
    x1: cython.int = (x // 1) % 10
    if x >= 10:
        x2: cython.int = (x // 10) % 10
        if x >= 100:
            x3: cython.int = (x // 100) % 10
            if x >= 1_000:
                x4: cython.int = (x // 1_000) % 10
                if x >= 10_000:
                    x5: cython.int = (x // 10_000) % 10
                    if x >= 100_000:
                        x6: cython.int = (x // 100_000) % 10
                        if x >= 1_000_000:
                            x7: cython.int = (x // 1_000_000) % 10
                            if x >= 10_000_000:
                                x8: cython.int = (x // 10_000_000) % 10
                                if x >= 100_000_000:
                                    x9: cython.int = (x // 100_000_000) % 10
                                    return x1, x2, x3, x4, x5, x6, x7, x8, x9
                                else:
                                    return x1, x2, x3, x4, x5, x6, x7, x8
                            else:
                                return x1, x2, x3, x4, x5, x6, x7
                        else:
                            return x1, x2, x3, x4, x5, x6
                    else:
                        return x1, x2, x3, x4, x5
                else:
                    return x1, x2, x3, x4
            else:
                return x1, x2, x3
        else:
            return x1, x2
    else:
        return x1,


_pows: cython.int[10]
_pows = [x ** x for x in range(9 + 1)]
_pows[0] = 0

def munchies(rng):
    a, b = rng
    # print([i for i in range(440_000_000) if (((not i % 1_000_000) and print(i) == None) or True) and sum(pows(x) for x in digits(i)) == i])
    # print([i for i in range(1_000_000) if sum(pows(x) for x in digits(i)) == i]) # NOTE: 0 is an artefact of sum([]) == 0
    #return [i for i in range(440_000_000) if (((not i % 1_000_000) and print(i) == None) or True) and sum(pows(x) for x in digits(i)) == i]
    r: cython.int[5] = [0]*5
    idx: cython.int = 0
    for i in range(a,b):
        if not i % 1_000_000:
            print(i)
        if sum(_pows[x] for x in digits(i)) == i:
            r[idx] = i
            i += 1
    return r