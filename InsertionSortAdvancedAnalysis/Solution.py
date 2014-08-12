#!/usr/bin/python3


if __name__ == '__main__':
    t = int(input())
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for _ in range(t):
        for i in range(1, n):
            v = l[i]
            j = i - 1
            while j >= 0 and (v < l[j]):
                l[j + 1] = l[j]
                l[j] = v
                j -= 1
                c += 1
        print(c)
