#!/usr/bin/python3


if __name__ == '__main__':
    l = int(input())
    r = int(input())
    m = -1
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            c = i ^ j
            if m < c:
                m = c
    print(m)
