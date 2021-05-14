A, B = list(map(lambda x: int(''.join(list(reversed(list(x))))), input().split()))

print(A if A > B else B)
