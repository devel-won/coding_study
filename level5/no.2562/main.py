B = []
count = 0

while count != 9:
    A = int(input())
    B.append(A)
    count += 1

max_value = max(B)

print(max_value)
print(B.index(max_value)+1)
