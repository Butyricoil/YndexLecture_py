# задача 3 выведите гистограмму каак в примере (коды символов отсортированы)
def printchar(s):
    symcount = {}
    macsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount [sym] += 1
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
        sorteduniqsyms = sorted(symcount.keys())
        for row in range(maxsymcount, 0, -1):
            for sym in sorteduniqsyms:
                if symcount [sym] >= row:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()
        print(''.join(sorteduniqsyms))
