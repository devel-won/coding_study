A = input().zfill(2)
B = None
count = 0

while A != B:
    if B is None:
        B = A
    a, b = int(B[0]), int(B[1])
    B = str(b) + str(a + b).zfill(2)[1]
    count += 1

print(count)
