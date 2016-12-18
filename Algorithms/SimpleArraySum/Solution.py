#!/usr/bin/python3


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(n) for n in input().strip().split(' ')]
    assert n == len(arr)
    result = 0

    for i in range(n):
        result += arr[i]

    print(result)
