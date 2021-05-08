A, B = list(map(int, input().split()))

result = "<" if (A < B) else ">" if (A > B) else "=="

print(result)