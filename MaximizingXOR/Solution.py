#!/usr/bin/python3


if __name__ == '__main__':
    l = int(input())
    r = int(input())
    p = l ^ r
    res = 1
    while(p):
        res <<= 1
        p >>= 1
    print(res - 1)
