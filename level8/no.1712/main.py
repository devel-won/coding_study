A, B, C = list(map(lambda x: int(x), input().split()))

print(int(A / (C - B)) + 1 if C > B else -1)
