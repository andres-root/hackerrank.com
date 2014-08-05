#!/usr/bin/python3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        w = list(input())
        r = 0
        i = 0
        j = len(w) - 1
        while i < j:
            r += abs(ord(w[i]) - ord(w[j]))
            i = i + 1
            j = j - 1
        print(r)
