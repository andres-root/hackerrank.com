#!/usr/bin/python3


if __name__ == '__main__':
    t = int(input())
    assert t >= 1
    assert t <= pow(10, 5)
    for _ in range(t):
        n = int(input())
        assert n >= 10
        assert n <= (4 * pow(10, 16))
        i = 0
        m = 1
        r = 0
        while i <= n:
            if i % 2 == 0:
                r += i
            f = m + i
            m = i
            i = f
        print(r)
