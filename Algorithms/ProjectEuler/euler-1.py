#!/usr/bin/python3


if __name__ == '__main__':
    t = int(input())
    assert t >= 1
    assert t <= pow(10, 5)
    for _ in range(t):
        n = int(input())
        assert n >= 1
        assert n <= pow(10, 9)
        i = int((n - 1) / 3)
        j = int((n - 1) / 5)
        k = int((n - 1) / 15)
        a = int((i * (3 + (3 * i))) / 2)
        b = int((j * (5 + (5 * j))) / 2)
        c = int((k * (15 + (15 * k))) / 2)
        print(int(a + b - c))
