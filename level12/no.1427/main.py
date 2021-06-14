import sys

N = list(sys.stdin.readline())

N.sort(reverse=True)

print(''.join(N))
