#!/usr/bin/python3


if __name__ == '__main__':
    t = int(input())
    assert t >= 1
    assert t <= 10
    for _ in range(t):
        k = int(input())
        assert k >= 2
        assert k <= pow(10, 7)
        if k % 2 == 0:
            print(k // 2 * k // 2)
        else:
            print((k // 2) * ((k // 2) + 1))
