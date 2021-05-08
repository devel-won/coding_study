A = int(input())
B = int(input())
result = 1 if (A > 0 and B > 0) else 2 if (A < 0 and B > 0) else 3 if (A < 0 and B < 0) else 4

print(result)
