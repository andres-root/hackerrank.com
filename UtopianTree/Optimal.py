#!/usr/bin/env python


for _ in range(input()):
    n = input()
    print pow(2, (n + 1) / 2 + 1) - 1 - (n % 2)
