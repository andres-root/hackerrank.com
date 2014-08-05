#!/usr/bin/python3


if __name__ == '__main__':
    n = int(input())
    assert n >= 1
    assert n <= 100
    s = []
    for _ in range(n):
        s.append(set(input()))
        r = set.intersection(*s)
    r = len(s)
    print(r)
