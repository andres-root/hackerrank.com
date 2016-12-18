#!/usr/bin/python3


if __name__ == '__main__':
    s = str(input())
    m = {}
    for c in s:
        if c in m:
            m[c] = not m[c]
        else:
            m[c] = False
    f = list(m.values()).count(False) == 1 or list(m.values()).count(False) == 0
    print('YES' if f else 'NO')
