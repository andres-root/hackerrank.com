#!/usr/bin/python3


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N, C, M = str(input()).split()
        total = int(N) // int(C)
        wrappers = total
        while(wrappers >= int(M)):
            chocolates = wrappers // int(M)
            wrappers = wrappers % int(M) + chocolates
            total += chocolates
        print(total)
