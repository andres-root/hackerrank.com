#!/usr/bin/python3


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    assert N >= 3
    assert N <= 10 ** 7
    assert M >= 1
    assert M <= 10 ** 5
    j = {}
    t = 0
    for _ in range(M):
        a, b, k = list(map(int, input().split()))
        assert b >= a
        assert b <= N
        assert a >= 1
        assert a <= b
        assert k >= 0
        assert k <= 10 ** 6
        t += (b + 1 - a) * k
    print(t // N)
