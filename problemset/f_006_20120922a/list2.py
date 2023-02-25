#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.


# D.
# Bemenet: számok rendezett listája.
# Kimenet: a bementből távolítsuk el az ismétlődéseket, vagyis az
# eredményben egy szám csak egyszer szerepeljen.
# Példa: [1, 2, 2, 3] -> [1, 2, 3].
# Készíthetünk egy új listát, vagy módosíthatjuk a bemeneti listát is.
def remove_adjacent(nums):
    return [x for i, x in enumerate(nums) if i == 0 or (i > 0 and x != nums[i-1])]

# E.
# Bemenet: két lista, mindkettőben az elemek növekvő sorrendbe rendezve.
# Kimenet: egy összefésült lista, melyben az elemek rendezve szerepelnek.
def list_merge(list1, list2):
    i1, i2 = 0, 0
    l = list()
    while i1 < len(list1) or i2 < len(list2):
        if i1 < len(list1):
            e1 = list1[i1]
        else:
            e1 = None
        if i2 < len(list2):
            e2 = list2[i2]
        else:
            e2 = None

        if e1 and e2 and e1 <= e2:
            l.append(e1)
            i1 += 1
        elif e1 and e2 and e2 < e1:
            l.append(e2)
            i2 += 1
        elif e1:
            l.append(e1)
            i1 += 1
        elif e2:
            l.append(e2)
            i2 += 1
    return l


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print()
    print('list_merge')
    test(list_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(list_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(list_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

#############################################################################

if __name__ == '__main__':
    main()