#!/usr/bin/python3


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(n) for n in input().strip().split(' ')]
    assert n == len(arr)
    assert n >= 1
    assert n <= 10
    result = 0

    for i in range(n):
        assert arr[i] >= 0
        assert arr[i] <= 10**10
        result += arr[i]

    print(result)
