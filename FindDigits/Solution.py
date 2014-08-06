#!/usr/bin/python3


if __name__ == '__main__':
    t = int(input())
    assert t >= 1
    assert t <= 15
    for _ in range(t):
        n = int(input())
        assert n > 0
        assert n < 10 ** 10
        c = 0
        for d in str(n):
            if int(d) > 0:
                if n % int(d) == 0:
                    c += 1
        print(c)
