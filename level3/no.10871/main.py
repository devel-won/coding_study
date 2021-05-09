import sys

N, X = list(map(int, sys.stdin.readline().split()))

A = list(map(int, sys.stdin.readline().split()))

for i in list(filter(lambda x: x < X, A)):
    print(i, end=' ')