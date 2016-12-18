N = int(input())
a = list(map(int, input().split()))

while len(a) > 0:
    a = [abs(min(a) - e) for e in a]
    print(len(a))
    a = [e for e in a if e != 0]
