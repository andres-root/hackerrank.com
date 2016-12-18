#!/usr/bin/python3


if __name__ == '__main__':
    N, T = list(map(int, input().split()))
    W = list(map(int, input().split()))
    for d in range(T):
        i, j = list(map(int, input().split()))
        print(min(W[i:j + 1]))
