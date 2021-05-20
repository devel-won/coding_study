A = int(input())

x = A // 5
result = -1

for i in range(x, -1, -1):
    if (A - 5 * i) % 3 == 0:
        result = int(i + ((A - 5 * i) // 3))
        break

print(result)
