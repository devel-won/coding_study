A = int(input())
N = int((A * 2) ** 0.5)
B = int(A - (N * (N - 1)) / 2)

while B > N:
    B = B - N
    N += 1

C = N + 1 - B

if N % 2 == 1:
    print(f"{C}/{B}")
else:
    print(f"{B}/{C}")
