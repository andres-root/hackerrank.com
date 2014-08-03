#!/usr/bin/python3


def Solution(n, s):
    if n == 0:
        return s
    else:
        for i in list(range(0, n + 1)):
            if i == 0:
                s = s
            else:
                if i % 2 == 0:
                    s += 1
                else:
                    s *= 2
    return s

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print(Solution(n, 1))
