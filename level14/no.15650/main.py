import sys


def d(in_list, r):
    for i in range(len(in_list)):
        if r == 1:
            yield [in_list[i]]
        else:
            tmp_list = in_list.copy()
            for j in d(tmp_list[i+1:], r-1):
                yield [in_list[i]] + j


N, M = map(int, sys.stdin.readline().strip().split())

A = [i for i in range(1, N+1)]

result = d(A, M)

for i in d(A, M):
    for j in i:
        print(j, end=' ')
    print()
