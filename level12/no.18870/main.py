import sys

N = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().strip().split()))

B = list(set(A))

B.sort()


def bs(input, start, end):
    mid = (start + end) // 2
    if input == B[mid]:
        return mid
    elif input < B[mid]:
        return bs(input, start, mid)
    else:
        return bs(input, mid, end)


for i in A:
    print(bs(i, 0, len(B)), end=' ')
