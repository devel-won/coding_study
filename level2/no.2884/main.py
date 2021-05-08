A, B = list(map(int, input().split()))

C = B - 45

A = A - 1 if C < 0 else A
A = 24 + A if A < 0 else A

B = 60 + C if C < 0 else C

print(A, B)